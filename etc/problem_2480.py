a, b, c = map(int, input().split())
if a == b == c:
    r = 10000 + a * 1000
elif a == b or b == c:
    r = 1000 + b * 100
elif c == a:
    r = 1000 + c * 100
else:
    r = max(a, b, c) * 100
print(r)
