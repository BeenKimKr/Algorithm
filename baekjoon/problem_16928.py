from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
b = [0] * 101
v = [False] * 101
q = deque([1])
l, s = {}, {}
for _ in range(N):
    x, y = map(int, input().split())
    l[x] = y
for _ in range(M):
    x, y = map(int, input().split())
    s[x] = y

while q:
    i = q.popleft()
    if i == 100:
        print(b[i])
        break
    for d in range(1, 7):
        p = i + d
        if p <= 100 and not v[p]:
            if p in l.keys():
                p = l[p]
            elif p in s.keys():
                p = s[p]
            if not v[p]:
                v[p] = True
                b[p] = b[i] + 1
                q.append(p)
