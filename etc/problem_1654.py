from sys import stdin

K, N = map(int, stdin.readline().split())
cables = []
for i in range(K):
    cables.append(int(stdin.readline().strip()))

answer = 0
start = 1
end = max(cables)

while start <= end:
    mid = (start + end) // 2  # 임시 길이
    c = 0  # mid값으로 만들 수 있는 케이블의 수

    for i in cables:
        c += i // mid

    if N <= c:
        start = mid + 1
        answer = max(answer, mid)
    else:
        end = mid - 1

print(answer)
