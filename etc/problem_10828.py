from collections import deque
import sys

N = int(input())
stack = deque()

for _ in range(N):
    order = sys.stdin.readline().strip()

    if order == 'pop':
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)
    elif order == 'size':
        print(len(stack))
    elif order == 'empty':
        if len(stack) != 0:
            print(0)
        else:
            print(1)
    elif order == 'top':
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)
    else:
        stack.append(int(order.split()[1]))
