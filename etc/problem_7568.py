from sys import stdin

N = int(input())
body = [list(map(int, stdin.readline().split())) for i in range(N)]
result = [0 for _ in range(N)]

for i in range(N):
    rank = 1
    p = body[i]  # 비교 기준
    for j in range(N):
        c = body[j]  # 모든 요소와 비교
        if i != j and c[0] > p[0] and c[1] > p[1]:
            rank += 1
    result[i] = str(rank)

print(' '.join(result))
