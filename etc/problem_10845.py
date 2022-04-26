from collections import deque
import sys

N = int(input())
queue = deque()

for _ in range(N):
    order = sys.stdin.readline().strip()

    if order == 'pop':
        if len(queue) != 0:
            print(queue.popleft())
        else:
            print(-1)
    elif order == 'size':
        print(len(queue))
    elif order == 'empty':
        if len(queue) != 0:
            print(0)
        else:
            print(1)
    elif order == 'front':
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)
    elif order == 'back':
        if len(queue) != 0:
            print(queue[-1])
        else:
            print(-1)
    else:
        queue.append(int(order.split()[1]))
