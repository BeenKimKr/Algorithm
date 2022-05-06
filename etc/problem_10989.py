import sys

N = int(input())
nums = [0 for _ in range(10001)]
for i in range(N):
    nums[int(sys.stdin.readline().strip())] += 1

idx = 0
for i in nums:
    if i != 0:
        for _ in range(i):
            print(idx)
    idx += 1
