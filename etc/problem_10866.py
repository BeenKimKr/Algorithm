import sys
from collections import deque

n = int(input())
order = [sys.stdin.readline().strip() for _ in range(n)]
d = deque()

for i in order:
    if i == 'pop_front':
        if len(d) == 0:
            print(-1)
        else:
            print(d.popleft())
    elif i == 'pop_back':
        if len(d) == 0:
            print(-1)
        else:
            print(d.pop())
    elif i == 'size':
        print(len(d))
    elif i == 'empty':
        if len(d) == 0:
            print(1)
        else:
            print(0)
    elif i == 'front':
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])
    elif i == 'back':
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])
    else:
        od, x = i.split()
        if od == 'push_front':
            d.appendleft(int(x))
        else:
            d.append(int(x))
