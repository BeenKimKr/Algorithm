line = input().split()
n, k = map(int, line)

circle = list(range(1, n + 1))
answer = []
idx = 0

while circle:
    idx = (idx + k - 1) % len(circle)
    answer.append(str(circle.pop(idx)))

print('<' + ', '.join(answer) + '>')
