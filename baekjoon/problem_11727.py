import sys
sys.setrecursionlimit(10**6)
n = int(input())
v = {1: 1, 2: 3}


def f(n):
    if n not in v:
        v[n] = f(n-1) + 2*f(n-2)
    return v[n] % 10007


print(f(n))
