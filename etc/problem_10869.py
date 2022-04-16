a, b = input().split()

for i in '+-*/%':
    print(int(eval(a+i+b)))
