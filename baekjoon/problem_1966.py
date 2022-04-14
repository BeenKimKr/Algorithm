import sys
from collections import deque

d = int(input())

for _ in range(d):
    n, m = map(int, sys.stdin.readline().split())
    queue = deque(list(map(int, sys.stdin.readline().split())))
    target = queue[m]
    cnt = 1

    while queue:
        first = max(queue)
        item = queue.popleft()
        m -= 1

        if len(queue) == 0:
            print(cnt)
            break
        elif item == first:
            if item == target and m == -1:
                print(cnt)
                break
            cnt += 1
        else:
            queue.append(item)
            m = len(queue) - 1 if m == -1 else m
