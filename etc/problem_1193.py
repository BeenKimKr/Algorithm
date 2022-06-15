X = int(input())
t = 1

while t < X:
    X -= t
    t += 1

if t % 2:
    a = t - X + 1
    b = X
else:
    a = X
    b = t - X + 1

print(f'{a}/{b}')
