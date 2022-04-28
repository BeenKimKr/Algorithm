import sys

N = int(input())
nums = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))
nums = sorted(nums, key=lambda x: (x[0], x[1]))
for i in range(N):
    print('{} {}'.format(nums[i][0], nums[i][1]))
