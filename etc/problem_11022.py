import sys
input = sys.stdin.readline

n = int(input())
for i in range(1, n+1):
    x, y = input().split()
    print('Case #' + str(i) + ': ' + x + ' + ' + y + ' =', int(x)+int(y))
