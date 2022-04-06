def getPoly(cnt):
    if cnt%2 != 0:
        return -1

    a = 'AAAA'
    b = 'BB'

    # board를 4로 나눈 몫을 aaaa, 그 나머지를 2로 나눈 몫을 bb, 나머지가 있으면 -1
    if cnt%4 == 0:
        return a * (cnt // 4)
    else:
        return a * (cnt // 4) + b * (cnt%4 // 2)

board = input()

cnt = 0
ptr = 0
poly = ''
res = ''

for i in board:
    if i == 'X':
        cnt += 1

    ptr += 1

    if i == '.' or (i == 'X' and len(board) == ptr):
        poly = getPoly(cnt)

        if poly == -1:
            res = poly
            break

        res += poly

        if i == '.':
            res += '.'
            cnt = 0

    
print(res)
