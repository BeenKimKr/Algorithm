M = int(input())
N = int(input())

prime = []

for i in range(M, N+1):
    for j in range(2, i+1):
        if i==j:
            prime.append(i)
        if i%j == 0:
            break

if not prime:
    print(-1)
else:
    print(sum(prime))
    print(min(prime))
    
