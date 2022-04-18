import sys

t = int(input())

for i in range(t):
    r, s = sys.stdin.readline().split()
    p = ''

    for j in s:
        p += str(j * int(r))
    
    print(p)
