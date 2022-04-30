import sys

N = int(sys.stdin.readline().strip())
nums = sorted(map(int, [sys.stdin.readline().strip() for _ in range(N)]))
for i in nums:
    print(i)
