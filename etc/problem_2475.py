code = input().split()
sum = 0

for i in code:
    sum += int(i)**2

print(sum % 10)
