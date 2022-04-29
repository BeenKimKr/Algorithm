import sys
from collections import deque

t = int(input())
ps = deque(list(sys.stdin.readline().strip() for _ in range(t)))

for i in ps:
    check = 0
    r_cnt = 0
    l_cnt = 0
    for j in i:
        if j == '(':
            r_cnt += 1
        elif j == ')':
            l_cnt += 1

        if r_cnt < l_cnt:
            print("NO")
            check += 1
            break

    if r_cnt == l_cnt:
        print("YES")
    elif check == 0:
        print("NO")
