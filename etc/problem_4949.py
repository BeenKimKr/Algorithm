from sys import stdin
from collections import deque

bracket = {'(': ')', '[': ']'}

while True:
    line = stdin.readline()
    if line == '.\n':
        break

    stack = deque([])
    check = True

    for i in line:
        if i in bracket.keys():
            stack.append(i)
        elif i in bracket.values():
            if not stack:
                check = False
                break
            if i != bracket[stack.pop()]:
                check = False
                break

    print('yes') if check and not stack else print('no')
