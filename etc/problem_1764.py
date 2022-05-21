from sys import stdin

N, M = map(int, stdin.readline().split())
unheard = set()
answer = []

for _ in range(N):
    unheard.add(stdin.readline().strip())
for _ in range(M):
    e = stdin.readline().strip()
    if e in unheard:
        answer.append(e)

answer.sort()
print(len(answer), '\n' + '\n'.join(answer))
