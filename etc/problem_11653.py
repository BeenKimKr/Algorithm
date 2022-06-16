import sys

N = int(input())
e = []
d = 2

while N > 1:
    if not N % d:
        e.append(d)
        N //= d
        sys.stdout.write(str(d)+'\n')
    else:
        d += 1
