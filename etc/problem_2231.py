n = int(input())
m = 0 if (n - len(str(n)) * 9) < 0 else (n - len(str(n)) * 9)
result = 0

while m <= n:
    if sum(map(int, str(m))) + m == n:
        result = m
        break
    m += 1

print(result)
