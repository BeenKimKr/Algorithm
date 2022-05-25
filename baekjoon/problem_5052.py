import sys
input = sys.stdin.readline

# 입력받은 케이스 list를 sort 후, 0번 index부터 검사 시작
# i번째 원소가 i+1의 i번째 원소길이만큼 slicing한 문자열과 같다면 일관성이 깨짐.
# 전부 검사하지 않고 다음 원소와 비교하며 O(N)으로 해결.
t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    m = [input().strip() for _ in range(n)]
    m.sort()

    for i in range(n-1):
        e = len(m[i])
        if m[i] == m[i+1][:e]:
            print('NO')
            break
    else:
        print('YES')
