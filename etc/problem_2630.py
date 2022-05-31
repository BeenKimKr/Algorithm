import sys
input = sys.stdin.readline

N = int(input())
p = [list(map(int, input().split())) for _ in range(N)]
w, b = 0, 0


def d(x, y, n):
    global w, b
    k = p[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if k != p[i][j]:
                d(x, y, n//2)
                d(x, y+n//2, n//2)
                d(x+n//2, y, n//2)
                d(x+n//2, y+n//2, n//2)
                return
    if k == 0:
        w += 1
    else:
        b += 1
    return


d(0, 0, N)
print(w)
print(b)
