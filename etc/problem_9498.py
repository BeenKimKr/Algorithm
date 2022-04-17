s = int(input()) # 점수
g = '' # 성적

if s >= 90:
    g = 'A'
elif s >= 80:
    g = 'B'
elif s >= 70:
    g = 'C'
elif s >= 60:
    g = 'D'
else:
    g = 'F'

print(g)
