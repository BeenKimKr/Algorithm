n = int(input())
c = 0

for i in range(1, n+1):
    if i < 100:
        c += 1
        continue

    s = str(i)
    if int(s[0]) - int(s[1]) == int(s[1]) - int(s[2]):
        c += 1

print(c)
