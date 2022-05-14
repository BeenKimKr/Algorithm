N = int(input())
sol = list(map(int, input().split()))
sol.sort()

s1 = 0  # 용액 특성값(작은 값)
s2 = 0  # 용액 특성값
s_abs = 2000000001  # 혼합한 용액 특성값의 절댓값(default는 최댓값)
left = 0
right = N - 1

# 혼합액 특성값을 비교
while left < right:
    mix = sol[left] + sol[right]

    if abs(mix) < s_abs:
        s_abs = abs(mix)
        s1 = sol[left]
        s2 = sol[right]

    if mix == 0:
        break
    elif mix < 0:
        left += 1
    else:
        right -= 1

print(s1, s2)
