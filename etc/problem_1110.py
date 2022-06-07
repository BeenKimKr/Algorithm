N = input()

x = N
c = 0
while True:
    a = int(x)//10
    b = int(x) % 10
    x = str(b) + str((a+b) % 10) if b != 0 else str((a+b) % 10)
    c += 1
    if x == N or x == '00':
        print(c)
        break
