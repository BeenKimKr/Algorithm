m, n = map(int, input().split())

for i in range(m, n+1):
    if i > 1:
        check = 0
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                check = 1
                break
        if check == 0:
            print(i)
