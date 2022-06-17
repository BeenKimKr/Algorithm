from math import sqrt
import sys
input = sys.stdin.readline

while True:
    n = int(input().strip())
    if n == 0:
        break

    c = 0
    for i in range(n+1, 2*n+1):
        v = True
        for j in range(2, int(sqrt(i))+1):
            if not i % j:
                v = False
                break
        if v and i != 1:
            c += 1
    print(c)
