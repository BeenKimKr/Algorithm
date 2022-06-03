A, B, C = map(int, input().split())
x = (A+B) % C
y = (A*B) % C
print('{}\n{}\n{}\n{}'.format(x, x, y, y))
