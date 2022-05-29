import sys
input = sys.stdin.readline
sys.setrecursionlimit(10*5)

# fibo()에서 c에 n이 있는지 확인
# 없으면 n을 key로 0과 1의 개수를 저장
# 재귀를 실행할 때마다 그 과정에 있는 수에 대한 결과를 저장하며 불필요한 호출을 줄인다.


def fibo(n):
    if n in c:
        return c[n]
    x = fibo(n-1)
    y = fibo(n-2)
    c[n] = [x[0]+y[0], x[1]+y[1]]
    return c[n]


N = int(input().strip())
for _ in range(N):
    num = int(input().strip())
    c = {0: [1, 0], 1: [0, 1]}
    a = fibo(num)
    print(a[0], a[1])
