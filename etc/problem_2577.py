a, b, c = list(int(input()) for _ in range(3))
mul = str(a*b*c)

for i in range(0, 10):
    print(mul.count(str(i)))
