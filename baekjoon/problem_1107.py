import sys
input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())
b = input().split()
res = abs(100-N)

for i in range(1000001):
    p = str(i)
    c = False
    for j in p:
        if j in b:
            c = True
            break
    if c:
        continue
    else:
        res = min(res, abs(N-i)+len(p))

print(res)
