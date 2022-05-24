N = int(input())

# Solution_1(38652KB, 580ms)
# 최댓값까지의 list를 만들고 3과 2의 최소공배수인 6을 우선으로 연산결과의 최솟값을 해당 수의 index로 저장.
max = 10**6 + 1
ex = [0]*(max)

for i in range(2, max):
    if i % 6 == 0:
        ex[i] = min(ex[i//3]+1, ex[i//2]+1, ex[i-1]+1)
    elif i % 3 == 0:
        ex[i] = min(ex[i//3]+1, ex[i-1]+1)
    elif i % 2 == 0:
        ex[i] = min(ex[i//2]+1, ex[i-1]+1)
    else:
        ex[i] = ex[i-1]+1

print(ex[N])

# Solution_2(30840KB, 72ms)
# 1 이상 수에 대한 연산 횟수를 dictionary의 value에 저장
# dict에 연산 횟수가 존재하면 return, 없는 경우 2와 3을 나눈 몫을 함수로 넘겨주며 재귀 호출 진행
# 입력 받은 수까지 재귀 호출을 하며 연산하는 방식이므로 실행시간이 1번 Solution보다 짧다. 입력의 최댓값도 없음.
ex = {1: 0, 2: 1}


def rec(n):
    if n in ex:
        return ex[n]
    ex[n] = 1 + min(rec(n//2) + n % 2, rec(n//3) + n % 3)
    return ex[n]


print(rec(N))
