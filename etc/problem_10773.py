from collections import deque
from sys import stdin

K = int(input())
stack = deque([])
result = 0

for _ in range(K):
    num = int(stdin.readline().strip())

    if num == 0:
        result -= stack.pop()
    else:
        stack.append(num)
        result += num

print(result)
