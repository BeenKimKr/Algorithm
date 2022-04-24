import math

n = int(input())
nums = list(map(int, input().split()))
prime = 0

for i in nums:
    if i == 1:
        continue
    elif i == 2:
        prime += 1
        continue
    limit = int(math.sqrt(i)) + 1 if i > 10 else i
    check = True
    for j in range(2, limit):
        if i != 1 and i % j == 0:
            check = False
            break
    if check == True:
        prime += 1

print(prime)
