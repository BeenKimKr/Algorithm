import sys

t = int(input())

for _ in range(t):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    apt = [[i for i in range(1, n + 1)]]

    for i in range(1, k):
        floor = list()
        for j in range(1, n + 1):
            floor.append(sum(apt[i - 1][:j]))
        apt.append(floor)
    
    print(sum(apt[-1]))
