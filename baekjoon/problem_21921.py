N, X = map(int, input().split())
visitors = list(map(int, input().split()))

left = 0
right = X - 1
part_sum = sum(visitors[:X])
result = part_sum  # 부분합의 최댓값
result_lst = [part_sum]  # 반복문에서 나온 최댓값들
day = 0

while right <= N - 2:
    part_sum -= visitors[left]
    left += 1
    right += 1
    part_sum += visitors[right]

    if result <= part_sum:
        result = part_sum
        result_lst.append(part_sum)

# result_lst는 오름차순이므로 맨뒤부터 검사
while len(result_lst) != 0:
    i = result_lst.pop(-1)
    if i == result:
        day += 1
    else:
        break

if result == 0:
    print('SAD')
else:
    print(result)
    print(day)
