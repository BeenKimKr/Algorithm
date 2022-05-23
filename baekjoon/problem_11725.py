import sys
sys.setrecursionlimit(10**9)


N = int(sys.stdin.readline().strip())
tree = [[] for _ in range(N+1)]
parents = [0 for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

# parents의 부모를 탐색, 없으면 부모를 설정하고, 다시 연결된 노드를 재귀호출하여 넘김.


def dfs(start, tree, parents):
    for i in tree[start]:
        if parents[i] == 0:
            parents[i] = start
            dfs(i, tree, parents)


dfs(1, tree, parents)

for i in range(2, N+1):
    print(parents[i])

# 참고 링크(https://yongku.tistory.com/entry/%EB%B0%B1%EC%A4%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-11725%EB%B2%88-%ED%8A%B8%EB%A6%AC%EC%9D%98-%EB%B6%80%EB%AA%A8-%EC%B0%BE%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%ACPython)
