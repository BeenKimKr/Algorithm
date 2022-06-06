import sys
input = sys.stdin.readline

n = int(input())
s = []
for _ in range(n):
    s.append(int(input()))
for i in sorted(s):
    print(i)
