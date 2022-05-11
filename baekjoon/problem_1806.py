N, S = map(int, input().split())
nums = list(map(int, input().split()))
head = 0
p = 0
part_sum = nums[0]  # 부분합
part_len = 1  # 부분합을 이루는 수열의 길이
result = 100001

while True:
    if part_sum >= S:
        if part_len < result:
            result = part_len
        part_sum -= nums[head]
        head += 1
        part_len -= 1
    else:
        p += 1
        if p >= N:
            break
        part_sum += nums[p]
        part_len += 1

print(0) if result == 100001 else print(result)
