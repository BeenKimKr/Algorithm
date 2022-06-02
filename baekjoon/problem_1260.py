import sys
from collections import deque
input = sys.stdin.readline

N, M, s = map(int, input().split())
v = [False]*(N+1)
g = [[] for _ in range(N+1)]
r = []

for _ in range(M):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
for i in range(len(g)):
    g[i].sort()


def dfs(s):
    r.append(str(s))
    v[s] = True
    for i in g[s]:
        if not v[i]:
            dfs(i)
            v[i] = True


def bfs(s):
    q = deque([s])
    v[s] = True
    while q:
        w = q.popleft()
        r.append(str(w))
        for i in g[w]:
            if not v[i]:
                q.append(i)
                v[i] = True


dfs(s)
print(' '.join(r))
v = [False]*(N+1)
r = []
bfs(s)
print(' '.join(r))
