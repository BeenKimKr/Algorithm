import sys

N = int(input())
students = [sys.stdin.readline().strip() for _ in range(N)]

# 1. 국어 내림차순
# 2. 영어 오름차순
# 3. 수학 내림차순
# 4. 이름 오름차순
students.sort(key=lambda x: (
    -int(x.split()[1]),
    int(x.split()[2]),
    -int(x.split()[3]),
    x.split()[0]
))

for i in students:
    print(i.split()[0])
