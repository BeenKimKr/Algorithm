h, m = map(int, input().split())
t = int(input())
print((h+(t+m)//60) % 24, (t+m) % 60)
