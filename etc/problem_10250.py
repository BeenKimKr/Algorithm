import sys

t = int(input())

for _ in range(t):
    h, w, n = map(int, sys.stdin.readline().split())

    floor = h if n % h == 0 else n % h
    room = n // h if n % h == 0 else n // h + 1

    print(f'{floor}{room:02d}')
