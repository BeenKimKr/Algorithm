from sys import stdin
N, M = map(int, stdin.readline().split())
trees = list(map(int, stdin.readline().split()))
start, end = -1, 1000000000

while start <= end:
    mid = (start + end) // 2
    logging = 0

    for i in trees:
        if i > mid:
            logging += i - mid

    if M <= logging:
        start = mid + 1
    else:
        end = mid - 1

print(end)
