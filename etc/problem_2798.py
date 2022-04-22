N, M = map(int, input().split())
card = list(map(int, input().split()))
best = 0

for i in range(len(card)):
    for j in range(i + 1, len(card)):
        for k in range(j + 1, len(card)):
            p = card[i] + card[j] + card[k]
            if p > best and p <= M:
                best = p

print(best)
