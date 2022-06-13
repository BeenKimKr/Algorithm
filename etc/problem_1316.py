import sys
input = sys.stdin.readline

N = int(input().strip())
c = 0

for _ in range(N):
    e = {}
    w = input().strip()
    t = ''
    for i in w:
        if i not in e.keys():
            e[i] = 1
        elif t != i and e[i] > 0:
            break
        else:
            e[i] += 1
        t = i
    if sum(e.values()) == len(w):
        c += 1

print(c)
