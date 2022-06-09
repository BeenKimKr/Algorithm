s = []


def d():
    for i in range(1, 10001):
        t = str(i)
        for j in t:
            i += int(j)
        s.append(i)


d()
for i in range(1, 10001):
    if i not in s:
        print(i)
