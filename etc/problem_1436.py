N = int(input())
cnt = 1
i = 666
while N != cnt:
    i += 1
    six = 0
    str_i = str(i)
    for j in range(len(str_i)-2):
        if str_i[j:j+3] == '666':
            cnt += 1
            break

print(i)
