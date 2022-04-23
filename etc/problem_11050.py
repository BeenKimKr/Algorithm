import math

n, k = map(int, input().split())
f = math.factorial
print(f(n) // (f(k) * f(n - k)))
