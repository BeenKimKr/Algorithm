from sys import stdin

N, M = map(int, stdin.readline().split())
info = {}

for _ in range(N):
    url, pw = stdin.readline().split()
    info[url] = pw

for _ in range(M):
    print(info[stdin.readline().strip()])
