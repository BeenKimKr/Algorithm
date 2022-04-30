import sys

N = int(sys.stdin.readline().strip())
num = sorted(map(int, [sys.stdin.readline().strip() for _ in range(N)]))
for i in num:
    print(i)
