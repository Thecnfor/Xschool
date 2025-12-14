import time
import random

# 蓝桥杯 Python A 组 - 时间复杂度实验室
# 目标：直观感受 O(n^2) 和 O(n) 的巨大差距
# 任务：在一个列表中找到两个数，使它们的和等于 target

def solve_n2(nums, target):
    """
    暴力解法：两层循环
    时间复杂度：O(n^2)
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None

def solve_n(nums, target):
    """
    优化解法：哈希表 (字典)
    时间复杂度：O(n) - 查找字典是 O(1)
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i
    return None

def run_test(size):
    print(f"\n--- 测试数据规模: {size} ---")
    
    # 生成随机数据
    nums = [random.randint(1, size * 2) for _ in range(size)]
    target = size * 3  # 故意设置一个较大的 target，增加查找难度
    
    # 强制让最后两个数匹配，确保 worst-case (最坏情况)
    nums[-2] = 100
    nums[-1] = 200
    target = 300

    # 测试 O(n)
    start_time = time.time()
    solve_n(nums, target)
    end_time = time.time()
    time_n = end_time - start_time
    print(f"O(n)   耗时: {time_n:.6f} 秒")

if __name__ == '__main__':
    # 蓝桥杯一般限制 1-2 秒
    # Python 1秒大约能跑 2*10^7 到 5*10^7 次简单运算
    run_test(30000000)