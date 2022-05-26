import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
# 한행씩 각 열로 갈 수 있는지 확인
# 어떤 한 행의 원소가 '1'이면서 해당 원소의 index행에 방문하지 않았다면(='0') '1'로 저장
# 해당원소의 index로 최대 깊이까지 재귀 호출


def f(x):
    for j in range(N):
        if g[x][j] == '1' and a[j] == '0':
            a[j] = '1'
            f(j)


N = int(input())
g = [input().split() for _ in range(N)]

for i in range(N):
    a = ['0' for _ in range(N)]
    f(i)
    print(' '.join(a))
