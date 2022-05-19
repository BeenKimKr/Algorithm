from sys import stdin

N, M = map(int, stdin.readline().split())
idx_dict = {}  # 구분 없이 한 개에 넣고, M개 줄의 입력에 따라 구분하는 방식도 가능
name_dict = {}

for i in range(1, N+M+1):
    n = stdin.readline().strip()
    if i <= N:
        idx_dict[i] = n
        name_dict[n] = i
    else:
        # isdigit() => 전부 숫자로 이뤄진 문자열이면 True를 반환
        if n.isdigit():
            print(idx_dict[int(n)])
        else:
            print(name_dict[n])
