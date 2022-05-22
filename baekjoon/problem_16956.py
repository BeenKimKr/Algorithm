from sys import stdin

R, C = map(int, stdin.readline().split())

answer = []
wolf = []  # 늑대들 위치
safe = 1  # 양들의 상태
idx_r = 0

# 입력을 받으며 문자열 내 양과 늑대가 서로 옆칸에 있는지 확인 + 늑대들 위치를 수집
for i in range(R):
    line = stdin.readline().strip().replace('.W', 'DW').replace('W.', 'WD')
    if 'WS' in line or 'SW' in line:
        safe = -1

    idx_c = 0
    for i in line:
        if i == 'W':
            wolf.append([idx_r, idx_c])
        idx_c += 1
    idx_r += 1
    answer.append(list(line))

# 수집된 늑대들 위치를 바탕으로 위아래 칸도 확인(행이 1일 경우는 필요X)
if safe == 1 and R > 1:
    for i in wolf:
        m, n = i

        # 맨위, 맨아래 행과 중간행 구분해서 확인
        if m == 0 or m == R-1:
            m = m + 1 if m == 0 else m - 1
            if answer[m][n] == '.':
                answer[m][n] = 'D'
            elif answer[m][n] == 'S':
                safe = -1
        else:
            for j in [-1, 1]:
                if answer[m+j][n] == '.':
                    answer[m+j][n] = 'D'
                elif answer[m+j][n] == 'S':
                    safe = -1

if safe == 1:
    print(1)
    for i in answer:
        print(''.join(i))
else:
    print(0)
