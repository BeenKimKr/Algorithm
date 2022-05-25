import sys
from collections import deque
input = sys.stdin.readline

case = int(input().strip())

for _ in range(case):
    order = list(input().strip())
    n = int(input().strip())
    d = deque(input()[1:-2].split(','))
    c = True  # 원소가 없음 + 'D'호출 에만 error발생
    r = 0  # 'R'(reverse)의 개수

    # 'R'일 때 r + 1
    # 'D'일 때 원소가 없다면 error출력, 반복종료
    # r이 홀수라면 reverse가 적용된 상태이므로 오른쪽에서 pop, 짝수라면 그대로이므로 왼쪽에서 pop
    # 함수 적용이 끝나고 r의 개수에 따라 reverse적용
    for i in order:
        if i == 'R':
            r += 1
        elif i == 'D':
            if n < 1:
                print('error')
                c = False
                break
            if r % 2:
                d.pop()
            else:
                d.popleft()
            n -= 1
    if c:
        if r % 2:
            d.reverse()
        print('[' + ','.join(d) + ']')
