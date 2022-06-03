input()
p = list(map(int, input().split()))
p.sort()
t = 0
a = 0
for i in p:
    t += i
    a += t
print(a)
