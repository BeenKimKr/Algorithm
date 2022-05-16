def getMinPrice(N, price):
    total = 0
    idx = 0

    for _ in range(N//3):
        total += sum(price[idx:idx+2])
        idx += 3

    if N % 3 != 0:
        total += sum(price[idx:])

    return total


N = int(input())
price = [int(input()) for _ in range(N)]

price = sorted(price, reverse=True)
res = sum(price) if N <= 2 else getMinPrice(N, price)

print(res)
