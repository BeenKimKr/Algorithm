import sys
input = sys.stdin.readline

N = int(input().strip())
s = [0] + [int(input().strip()) for _ in range(N)]

# 계단이 한칸일 경우 0부터 list에 입력 받았으므로 1번째 칸을 출력
# 첫번째 칸을 무조건 밟아야 하기 때문에 한칸과 두칸 합을 먼저 저장
# 그 외, list를 돌며 현재 위치에서 i-3번째까지의 합 + i-1번째와 i-2번째까지의 점수합 중 더 큰 값을 더해 i번째까지의 합에 저장
# 정신없이 푸느라 사소한 실수도 많았고 다소 헤맸던 문제였다. 비슷한 코드를 보기도 하고 해설을 참고해도 어디서 오류가 나는지 몰라서 디버깅을 한참 돌렸다..
# 도움받은 블로그
# https://kyoung-jnn.tistory.com/entry/%EB%B0%B1%EC%A4%802579%EB%B2%88%ED%8C%8C%EC%9D%B4%EC%8D%ACPython-%EA%B3%84%EB%8B%A8-%EC%98%A4%EB%A5%B4%EA%B8%B0-DP
if N == 1:
    print(s[0])
else:
    dp = [0] * (N+1)
    dp[1] = s[1]
    dp[2] = s[1] + s[2]

    for i in range(3, N+1):
        dp[i] = max(dp[i-3] + s[i-1] + s[i], dp[i-2] + s[i])

    print(dp[N])
