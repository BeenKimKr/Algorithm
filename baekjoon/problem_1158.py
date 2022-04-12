line = input().split()
n, k = map(int, line)

circle = list(range(1, n + 1))
answer = []
idx = 0

# k번째 index만 가져옴
# index가 리스트를 초과하는 경우 => index를 그 초과분으로 초기화
while circle:
    idx = (idx + k - 1) % len(circle)
    answer.append(str(circle.pop(idx)))

print('<' + ', '.join(answer) + '>')
