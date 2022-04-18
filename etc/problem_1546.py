n = int(input())
scores = list(map(int, input().split()))
print(sum(scores) / n / max(scores) * 100)
