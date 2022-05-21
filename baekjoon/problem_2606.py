from sys import stdin

N = int(stdin.readline().strip())
C = int(stdin.readline().strip())

# 컴퓨터 별 리스트 생성
total = [[] for _ in range(N)]

for i in range(C):
    a, b = map(int, stdin.readline().split())
    total[a-1].append(b)
    total[b-1].append(a)

stack = total[0]  # 1번 컴퓨터와 직간접적으로 연결된, 확인이 필요한 컴퓨터들
visited = []  # 감염여부 확인된 컴퓨터들

while stack:
    k = stack.pop(-1)
    # 확인된 컴퓨터는 pass(아래 조건문으로 불필요한 확인x)
    if k in visited:
        continue
    visited.append(k)

    # 연결된 컴퓨터를 확인, 추가로 연결된 컴퓨터가 있으면 stack에 추가
    for i in total[k-1]:
        if i in stack or i == 1:
            continue
        stack.append(i)

print(len(visited))
