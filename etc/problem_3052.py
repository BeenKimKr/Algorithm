import sys

result = []

for i in range(10):
    num = int(sys.stdin.readline().strip()) % 42

    if num not in result:
        result.append(num)
    
print(len(result))
