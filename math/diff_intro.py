"""
微分入门（数分考点→代码→建模）

本脚本用“导数的极限定义”做数值近似，展示：
- 导数定义：f'(x0) = lim_{h->0} (f(x0+h)-f(x0))/h
- 不同差分法（前向/后向/中心）
- 误差来源：截断误差 vs 浮点舍入误差（h过小会不稳定）
- 不可导点示例：f(x)=|x| 在 x=0 处不可导（单侧导数不同）

运行：
conda activate anx
python math/diff_intro.py

考点图谱：
1) 导数定义与可导性判定
2) 单侧导数与不可导示例（绝对值、尖点）
3) 数值近似的稳定性（选取步长）

和期末关系：本脚本直接对应“导数定义/单侧导数/可导性判定/误差分析”高频题。
"""

import math
from typing import Callable, List, Optional, Tuple


def forward_diff(f: Callable[[float], float], x: float, h: float) -> float:
    """前向差分"""
    return (f(x + h) - f(x)) / h


def backward_diff(f: Callable[[float], float], x: float, h: float) -> float:
    """后向差分"""
    return (f(x) - f(x - h)) / h


def central_diff(f: Callable[[float], float], x: float, h: float) -> float:
    """中心差分（通常精度更高）"""
    return (f(x + h) - f(x - h)) / (2.0 * h)


def derivative_by_definition(
    f: Callable[[float], float],
    x0: float,
    method: str = "central",
    h0: float = 1e-1,
    steps: int = 20,
) -> List[Tuple[float, float]]:
    """
    用差分近似导数，并返回(h, 近似导数)序列。

    method: "forward" | "backward" | "central"
    h 序列：h_k = h0 / 2^k
    """
    approx = []
    for k in range(steps):
        h = h0 / (2 ** k)
        if method == "forward":
            d = forward_diff(f, x0, h)
        elif method == "backward":
            d = backward_diff(f, x0, h)
        else:
            d = central_diff(f, x0, h)
        approx.append((h, d))
    return approx


def print_table(
    title: str,
    rows: List[Tuple[float, float]],
    true_derivative: Optional[float] = None,
):
    print("\n" + title)
    print("h\t近似导数\t误差(若有)")
    for h, d in rows:
        if true_derivative is None:
            print(f"{h:.3e}\t{d:.8f}")
        else:
            err = abs(d - true_derivative)
            print(f"{h:.3e}\t{d:.8f}\t{err:.3e}")


def demo_quadratic():
    """
    f(x) = x^2 在 x0 = 3 处，真导数 f'(x0) = 2*x0 = 6
    展示前/后/中心差分，以及误差随 h 的变化。
    """
    f = lambda x: x * x
    x0 = 3.0
    true = 2.0 * x0

    rows_f = derivative_by_definition(f, x0, method="forward", h0=1e-1, steps=20)
    rows_b = derivative_by_definition(f, x0, method="backward", h0=1e-1, steps=20)
    rows_c = derivative_by_definition(f, x0, method="central", h0=1e-1, steps=20)

    print_table("[示例1] f(x)=x^2, x0=3 的前向差分", rows_f, true)
    print_table("[示例1] f(x)=x^2, x0=3 的后向差分", rows_b, true)
    print_table("[示例1] f(x)=x^2, x0=3 的中心差分", rows_c, true)

    print("\n要点：中心差分通常比前/后向更精确；当 h 过小（接近机器精度），浮点舍入误差使误差反而增大。")


def demo_abs():
    """
    f(x) = |x| 在 x0 = 0 处不可导：
    - 右导数 lim_{h->0+} (|h|-0)/h = 1
    - 左导数 lim_{h->0+} (0-|(-h)|)/h = -1
    - 中心差分在数值上会接近 0，但不代表可导，因为单侧极限不同。
    """
    f = lambda x: abs(x)
    x0 = 0.0

    rows_f = derivative_by_definition(f, x0, method="forward", h0=1e-1, steps=20)
    rows_b = derivative_by_definition(f, x0, method="backward", h0=1e-1, steps=20)
    rows_c = derivative_by_definition(f, x0, method="central", h0=1e-1, steps=20)

    print_table("[示例2] f(x)=|x|, x0=0 的前向差分(近右导)", rows_f, None)
    print_table("[示例2] f(x)=|x|, x0=0 的后向差分(近左导)", rows_b, None)
    print_table("[示例2] f(x)=|x|, x0=0 的中心差分", rows_c, None)

    print("\n要点：单侧导数不同 ⇒ 不可导。中心差分给出 0 并不表示可导，判定必须看左右极限是否相等。")


def demo_rate_of_change():
    """
    建模视角：瞬时变化率
    例：位移 s(t) = sin(t) + 0.1*t 在 t0=1.0 的速度≈导数 s'(t0)
    （用中心差分近似速度，h 选取不要太大也不要太小）
    """
    s = lambda t: math.sin(t) + 0.1 * t
    t0 = 1.0
    rows_c = derivative_by_definition(s, t0, method="central", h0=1e-1, steps=15)
    # 真导数：s'(t) = cos(t) + 0.1
    true = math.cos(t0) + 0.1
    print_table("[示例3] s(t)=sin(t)+0.1t 的中心差分近似速度", rows_c, true)
    print("\n要点：导数 = 瞬时变化率；在物理建模中就是速度/加速度等。")


def main():
    print("微分入门：导数定义→差分近似→误差分析→不可导判定→建模")
    demo_quadratic()
    demo_abs()
    demo_rate_of_change()


if __name__ == "__main__":
    main()