import sys

# 蓝桥杯 Python A 组 - 快速上手模板
# 核心原则：
# 1. 只能使用 Python 标准库 (不能用 numpy, pandas 等)
# 2. 必须处理标准输入 (sys.stdin) 和标准输出 (print)
# 3. 效率至上 (Python 运行慢，需要优化 I/O 和算法)

def solve():
    # 题目：输入包含多组数据。每组数据包含一行，为两个整数 a 和 b。
    # 对于每组数据，输出 a + b 的值。
    
    # 技巧：sys.stdin.read().split() 可以一次性读取所有输入并按空白分割
    # 这比一行行读要快得多，适合绝大多数题目
    # 注意：在某些 Windows 环境下，输入可能包含 BOM 字符 (\ufeff)，需要处理
    content = sys.stdin.read()
    if content.startswith('\ufeff'):
        content = content[1:]
    input_data = content.split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        while True:
            # 尝试获取下一个 a 和 b
            a = int(next(iterator))
            b = int(next(iterator))
            print(a + b)
    except StopIteration:
        pass

if __name__ == '__main__':
    solve()
