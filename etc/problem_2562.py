import sys

large = 0
idx = 0

for i in range(9):
    num = int(sys.stdin.readline().strip())
    
    if large < num:
        large = num
        idx = i + 1

print('{}\n{}'.format(large, idx))
