N = int(input())
end = 1
lev = 0

while True:
    if end >= N:
        print(lev) if end != 1 else print(1)
        break
    
    end += 6 * lev
    lev += 1
