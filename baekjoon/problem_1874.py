import sys

n = int(sys.stdin.readline())
input = [ sys.stdin.readline().strip() for _ in range(n) ]

input = list(map(int, input))
check = [ i for i in input ]
input.reverse() # input이나 stack list에서 index 0값을 삭제시(pop) 리스트 재배열로 인한 시간복잡도 상승 => 맨뒤에서 pop

prev = check[0]  # 반복에서 이전 값
correct = True  # 출력문 조건
res = []  # 결과값 list
stack = []  # 스택 순서 확인
cnt = 1  # 스택 입력 값, for i in range(n) 으로도 작성 가능

for i in check:
    if i == prev:
        for _ in range(i):
            res.append('+')
            stack.append(cnt)
            cnt += 1
    elif i > prev:
        for _ in range(i-prev):
            res.append('+')
            stack.append(cnt)
            cnt += 1
        prev = i

    if i != stack[-1]:
        correct = False
        print("NO")
        break

    res.append('-')
    del input[-1]
    del stack[-1]

    if len(input) < 1:
        break

if correct:
    for i in range(len(res)):
        sys.stdout.write(str(res[i])+'\n')
