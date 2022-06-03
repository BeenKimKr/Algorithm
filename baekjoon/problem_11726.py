import sys
sys.setrecursionlimit(10**6)
n = int(input())
v = {1: 1, 2: 2}


def f(n):
    if n not in v:
        v[n] = f(n-1) + f(n-2)
    return v[n]


print(f(n) % 10007)
