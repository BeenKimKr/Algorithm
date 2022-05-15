N, K = map(int, input().split())
nums = list(map(int, input().split()))

left, right, result = 0, 0, 0
odd_cnt, even_cnt = 0, 0  # 부분 수열 내 홀수, 짝수

while True:
    # right는 홀수가 K개일 때까지 중가
    if nums[right] % 2 != 0:
        odd_cnt += 1
    else:
        even_cnt += 1

    right += 1
    # 끝에 도달
    if right == N:
        result = max(result, even_cnt)
        break

    # 홀수가 K보다 커질 경우 부분 수열엔 K개의 홀수가 존재하므로 결과에 저장
    # left 이동 후 이전 위치의 수를 even_cnt에 반영할지 판별
    if odd_cnt > K:
        result = max(result, even_cnt)
        left += 1
        if nums[left-1] % 2 == 0:
            even_cnt -= 1
        else:
            odd_cnt -= 1

print(result)
