import sys

N = int(input())
coor = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
coor.sort(key=lambda x: (int(x[1]), int(x[0])))

for i in coor:
    sys.stdout.write('{} {}\n'.format(i[0], i[1]))
