a, b, c, = map(int, input().split())
print(-1) if b >= c else print(int(a/(c-b)-1))
