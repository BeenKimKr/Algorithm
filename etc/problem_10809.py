s = input()
result = list(-1 for i in range(26))
cnt = 0

for i in s:
    idx = ord(i) - 97

    if result[idx] == -1:
        result[idx] = cnt

    cnt += 1

print(' '.join(map(str, result)))
