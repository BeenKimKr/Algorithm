from sys import stdin

N = int(stdin.readline().strip())
nums = []
ar = 0  # 산술평균
me = 0  # 중앙값
ra = 0  # 범위
mo = 0  # 최빈값
mo_dict = {}  # 빈도 dict

for i in range(N):
    n = int(stdin.readline().strip())
    ar += n
    nums.append(n)

    if n in mo_dict.keys():
        mo_dict[n] += 1
    else:
        mo_dict[n] = 1

if N == 1:
    print('{}\n{}\n{}\n{}'.format(ar, ar, ar, 0))
else:
    nums.sort()
    # value, key를 각각 내림차순, 오름차순으로 정렬(list -> dict)
    sorted_dict = dict(sorted(mo_dict.items(), key=lambda x: (-x[1], x[0])))

    ar = round(ar / N)
    me = nums[N//2]
    ra = nums[-1] - nums[0]

    # 최빈값 중 두 번째로 작은 값 추출
    if list(sorted_dict.values())[0] == list(sorted_dict.values())[1]:
        mo = list(sorted_dict.keys())[1]
    else:
        mo = list(sorted_dict.keys())[0]

    print('{}\n{}\n{}\n{}'.format(ar, me, mo, ra))
