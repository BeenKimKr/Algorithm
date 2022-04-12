import sys

N = int(input())
plans = [ sys.stdin.readline().split() for _ in range(N) ]

myPlans = [ list(map(int, i)) for i in plans ]
myPlans.sort(key=lambda x: (x[0], -x[1]))

calendar = [ list() for _ in range(myPlans[-1][1]) ]
idx = 1
width = 0
height = 0
total = 0
cnt = 0

for lst in myPlans:
    for j in range(lst[0]-1, lst[1]):
        # 계층 나누는 조건 필요
        calendar[j].append(idx)
    idx += 1

for i in calendar:
    if height < len(i):
        height = len(i)
    if width == 0 and len(i) == 0:
        continue
    elif width == 0 and len(i) > 0:
        width = 1
    elif width >= 1 and len(i) > 0:
        width += 1
    if (width >= 1 and len(i) == 0) or i == calendar[-1]:
        total += width * height
        width = 0
        height = 0
        print('total: ', total)
    
print(calendar)
