n, x = map(int, input().split())
nums = input().split()
answer = []

for i in nums:
    if int(i) < x:
        answer.append(i)

print(' '.join(answer))
