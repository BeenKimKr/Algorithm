import sys

while True:
    num = sys.stdin.readline().strip()
    comp = num[-1::-1]

    if num == '0':
        break
    elif num[-1] == '0' or num != comp:
        print('no')
    elif num == comp:
        print('yes')
