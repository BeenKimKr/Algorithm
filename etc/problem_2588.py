x = int(input())
y = input()
t = 1
a = 0
for i in range(2, -1, -1):
    b = x*int(y[i])
    print(b)
    a += b*t
    t *= 10
print(a)
