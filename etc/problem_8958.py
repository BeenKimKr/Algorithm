import sys

n = int(input())
score = 0

for _ in range(n):
    quiz = sys.stdin.readline()
    cnt = 0

    for i in quiz:
        cnt = cnt + 1 if i == 'O' else 0
        score += cnt

    if cnt != 0:
        score += cnt

    print(score)
    score = 0
