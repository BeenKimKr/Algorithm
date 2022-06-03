N = int(input())
x = list(map(int, input().split()))
y = sorted(list(set(x)))
d = {}

for i in range(len(y)):
    d[y[i]] = str(i)

for i in x:
    print(d[i], end=' ')
