from collections import deque
from sys import stdin


def findRoute(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            a, b = x + p1[i], y + p2[i]

            if a < 0 or a >= N or b < 0 or b >= M or maze[a][b] == 0:
                continue
            if maze[a][b] == 1:
                maze[a][b] = maze[x][y] + 1
                queue.append((a, b))

    return maze[N-1][M-1]


N, M = map(int, stdin.readline().split())
maze = [list(map(int, stdin.readline().strip())) for _ in range(N)]
p1 = [0, 1, 0, -1]
p2 = [1, 0, -1, 0]
print(findRoute(0, 0))
