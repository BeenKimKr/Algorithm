N = int(input())
members = [ input() for _ in range(N) ]
members.sort(key=lambda x: int(x.split()[0]))

for i in members:
    print(i)
