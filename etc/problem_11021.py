import sys
input = sys.stdin.readline
n = int(input())
for i in range(1, n+1):
    print('Case #'+str(i)+':', sum(map(int, input().split())))
