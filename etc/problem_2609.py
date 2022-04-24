a, b = map(int, input().split())
x, y = [a, b]
gcd = 1
i = 2

while True:
    if x % i == 0 and y % i == 0:
        x /= i
        y /= i
        gcd *= i
    else:
        i += 1

    if (a == 1 or b == 1) or i > min(a, b):
        break

print(gcd)
print(int(a * b // gcd))  # lcm
