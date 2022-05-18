from sys import stdin

N, M, B = map(int, stdin.readline().split())
ground = [list(map(int, stdin.readline().split())) for _ in range(N)]
time, height = 0, 0
answer = 64000000 * 250000 * 2 + 1

for i in range(267):
    g = 0  # 블록을 캐서 인벤토리에 넣기
    s = 0  # 인벤토리에서 블록을 꺼내서 놓기
    for n in range(N):
        for m in range(M):
            if ground[n][m] < i:
                s += i - ground[n][m]
            else:
                g += ground[n][m] - i

    # 놓을 블록 수가 가지고 있는 것보다 많은 경우 continue
    if g + B < s:
        continue

    time = s + g * 2
    if time <= answer:
        answer = time
        height = i

print(answer, height)
