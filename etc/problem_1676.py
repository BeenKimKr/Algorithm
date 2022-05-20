from math import factorial

N = int(input())
f = str(factorial(N))
answer = 0

for i in range(len(f)-1, -1, -1):
    if f[i] == '0':
        answer += 1
    else:
        break

print(answer)
