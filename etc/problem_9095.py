import sys
input = sys.stdin.readline

# N을 구성하는 1, 2, 3으로 만든 조합의 수를 재귀호출하며 저장하고 반환하는 간단한 dp문제다.
# + f(n-3)이 아니라 + (n-3)으로 작성하는 바람에 살짝 헤맸지만...


def f(n):
    if n < 1:
        return 0
    if n in d:
        return d[n]
    d[n] = f(n-1) + f(n-2) + f(n-3)
    return d[n]


N = int(input().strip())
for _ in range(N):
    m = int(input().strip())
    d = {1: 1, 2: 2, 3: 4}
    print(f(m))
