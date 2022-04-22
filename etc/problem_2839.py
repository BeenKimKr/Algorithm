n = int(input())
answer = -1

for i in range(n // 5, -1, -1):
    for j in range(n // 3 + 1):
        total = i * 5 + j * 3
        if total == n:
            answer = i + j
            break

    if answer != -1:
        break

print(answer)
