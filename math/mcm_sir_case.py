"""
数学建模竞赛编程手的完整案例（考点→代码→建模）

主题：疫情传播与防控策略优化（SIR 模型）

目标：从零到一完成一次“可复现”的端到端流程：
1) 明确问题与指标：拟合历史数据，预测未来趋势，评估干预策略
2) 数据处理：合成数据、训练/测试划分
3) 建模：SIR 常微分方程 + 欧拉数值解
4) 参数估计：网格搜索最小二乘拟合 β, γ
5) 评估：RMSE, R^2；与基线模型对比
6) 情景分析：降低传染率（β）模拟干预效果
7) 输出结论与建议：用于论文的“结果与讨论”部分

运行：
conda activate anx
python math/mcm_sir_case.py

期末/竞赛考点映射：
- 常微分方程数值求解（欧拉/步长选择/稳定性）
- 参数估计（最小二乘/网格搜索/过拟合与验证）
- 指标设计（RMSE、R^2）
- 情景分析与敏感性（改变 β 代表不同防控强度）
"""

import math
import random
from typing import List, Tuple, Dict


def sir_step(S: float, I: float, R: float, beta: float, gamma: float, N: float, dt: float) -> Tuple[float, float, float]:
    """SIR 单步欧拉离散。"""
    dS = -beta * S * I / N
    dI = beta * S * I / N - gamma * I
    dR = gamma * I
    S_next = S + dS * dt
    I_next = I + dI * dt
    R_next = R + dR * dt
    # 保证非负与不超过总量
    S_next = max(0.0, min(N, S_next))
    I_next = max(0.0, min(N, I_next))
    R_next = max(0.0, min(N, R_next))
    return S_next, I_next, R_next


def simulate_sir(beta: float, gamma: float, S0: float, I0: float, R0: float, N: float, days: int, dt: float = 1.0) -> List[float]:
    """模拟 days 天的 I(t)，按天记录。"""
    S, I, R = S0, I0, R0
    result_I = []
    for day in range(days):
        result_I.append(I)
        S, I, R = sir_step(S, I, R, beta, gamma, N, dt)
    return result_I


def generate_synthetic_data(beta: float, gamma: float, S0: float, I0: float, R0: float, N: float, days: int, noise_scale: float = 0.05) -> List[float]:
    """用真参数生成合成观测数据，并加入噪声（近似高斯比例噪声）。"""
    clean_I = simulate_sir(beta, gamma, S0, I0, R0, N, days)
    observed = []
    for I in clean_I:
        noise = random.gauss(0.0, noise_scale * max(1.0, I))
        y = max(0.0, I + noise)
        observed.append(y)
    return observed


def rmse(y_true: List[float], y_pred: List[float]) -> float:
    n = len(y_true)
    return math.sqrt(sum((yt - yp) ** 2 for yt, yp in zip(y_true, y_pred)) / n)


def r2_score(y_true: List[float], y_pred: List[float]) -> float:
    mean_y = sum(y_true) / len(y_true)
    ss_tot = sum((yt - mean_y) ** 2 for yt in y_true)
    ss_res = sum((yt - yp) ** 2 for yt, yp in zip(y_true, y_pred))
    if ss_tot == 0:
        return 0.0
    return 1.0 - ss_res / ss_tot


def fit_parameters_grid(
    y_train: List[float],
    S0: float,
    I0: float,
    R0: float,
    N: float,
    days: int,
    beta_grid: List[float],
    gamma_grid: List[float],
) -> Dict[str, float]:
    """网格搜索拟合 β, γ，以训练集 RMSE 最小为准。"""
    best = {"beta": None, "gamma": None, "rmse": float("inf")}
    for beta in beta_grid:
        for gamma in gamma_grid:
            pred = simulate_sir(beta, gamma, S0, I0, R0, N, days)
            loss = rmse(y_train, pred)
            if loss < best["rmse"]:
                best["rmse"] = loss
                best["beta"] = beta
                best["gamma"] = gamma
    return best


def baseline_last_value(y_train: List[float], horizon: int) -> List[float]:
    """简单基线：未来预测为训练末值的常量（竞赛中用于 sanity check）。"""
    last = y_train[-1]
    return [last for _ in range(horizon)]


def scenario_reduce_beta(beta: float, factor: float) -> float:
    """情景分析：降低传染率，factor∈(0,1]。"""
    factor = max(0.0, min(1.0, factor))
    return beta * factor


def main():
    random.seed(42)
    print("数学建模端到端案例：SIR 参数拟合与情景分析")

    # 1) 问题与数据设定（合成数据模拟真实竞赛数据场景）
    N = 1_000_000  # 总人口
    S0 = N - 1000
    I0 = 1000
    R0 = 0
    true_beta = 0.25  # 传染率
    true_gamma = 0.08  # 康复率
    total_days = 60
    observed_I = generate_synthetic_data(true_beta, true_gamma, S0, I0, R0, N, total_days, noise_scale=0.08)

    # 2) 划分训练/测试（防止过拟合，留出外推评估）
    train_days = 40
    test_days = total_days - train_days
    y_train = observed_I[:train_days]
    y_test = observed_I[train_days:]

    # 3) 网格设定（竞赛中可逐步加密网格或用更先进优化）
    beta_grid = [0.1 + 0.01 * i for i in range(20)]  # 0.10 ~ 0.29
    gamma_grid = [0.05 + 0.005 * i for i in range(20)]  # 0.05 ~ 0.145

    # 4) 拟合参数
    best = fit_parameters_grid(y_train, S0, I0, R0, N, train_days, beta_grid, gamma_grid)
    est_beta, est_gamma, train_rmse = best["beta"], best["gamma"], best["rmse"]

    # 5) 训练拟合与测试外推
    pred_train = simulate_sir(est_beta, est_gamma, S0, I0, R0, N, train_days)
    # 用训练集末状态作为测试起点（竞赛中要注意状态延续）
    S_last, I_last, R_last = S0, I0, R0
    for _ in range(train_days):
        S_last, I_last, R_last = sir_step(S_last, I_last, R_last, est_beta, est_gamma, N, 1.0)
    pred_test = simulate_sir(est_beta, est_gamma, S_last, I_last, R_last, N, test_days)

    # 6) 评估与基线对比
    train_r2 = r2_score(y_train, pred_train)
    test_rmse = rmse(y_test, pred_test)
    test_r2 = r2_score(y_test, pred_test)
    baseline_pred = baseline_last_value(y_train, test_days)
    baseline_rmse = rmse(y_test, baseline_pred)

    # 7) 情景分析：降低 β（例如 20%、40% 干预强度）
    beta_80 = scenario_reduce_beta(est_beta, 0.8)
    beta_60 = scenario_reduce_beta(est_beta, 0.6)
    scen80_test = simulate_sir(beta_80, est_gamma, S_last, I_last, R_last, N, test_days)
    scen60_test = simulate_sir(beta_60, est_gamma, S_last, I_last, R_last, N, test_days)

    # 8) 关键结果输出（用于论文的结果与讨论）
    R0_est = est_beta / est_gamma if est_gamma else float("inf")
    print("\n[参数估计]")
    print(f"估计 β={est_beta:.3f}, γ={est_gamma:.3f}, 训练RMSE={train_rmse:.2f}, 训练R2={train_r2:.3f}, R0≈{R0_est:.2f}")

    print("\n[测试集表现]")
    print(f"模型 Test RMSE={test_rmse:.2f}, Test R2={test_r2:.3f}; 基线 RMSE={baseline_rmse:.2f}")

    print("\n[情景分析：降低传染率]")
    print("干预20% (β×0.8) 下未来趋势(前5天I)：", [round(v) for v in scen80_test[:5]])
    print("干预40% (β×0.6) 下未来趋势(前5天I)：", [round(v) for v in scen60_test[:5]])

    print("\n[竞赛写作建议]")
    print("1) 方法部分：给出SIR方程、参数含义、离散化方法、拟合策略（网格/最小二乘）。")
    print("2) 结果部分：展示训练/测试表现、与基线对比、R0评估、情景分析曲线与峰值变化。")
    print("3) 讨论部分：模型假设、局限（未分年龄/空间异质性）、改进方向（SEIR、参数时变）。")

    print("\n[编程手角色与流程清单]")
    print("- 需求对齐：和队友确认问题拆解、指标与验证方法。")
    print("- 数据处理：清洗、缺失填补、特征工程、训练测试划分。")
    print("- 快速基线：实现简单可解释基线，锁定指标与评估框架。")
    print("- 模型实现：SIR/SEIR/回归/优化等主模型，写成可重复脚本。")
    print("- 参数估计：搜索/优化，记录超参数与随机种子，保证复现实验。")
    print("- 情景分析：参数扰动（β下降）、策略比较，输出可用于论文的图表数据。")
    print("- 写作支持：生成表格/关键数字、保存中间结果，便于队友写作。")
    print("- 版本管理：保持math/目录结构清晰，保证一键可运行。")


if __name__ == "__main__":
    main()