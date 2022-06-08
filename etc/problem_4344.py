import sys
input = sys.stdin.readline

C = int(input().strip())
for _ in range(C):
    s = list(map(int, input().split()))
    n = s[0]
    del s[0]
    a = sum(s)/n
    m = 0
    for i in s:
        if a < i:
            m += 1
    print('{:.3f}%'.format(m/n*100))
