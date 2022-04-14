import sys
from collections import deque

n = int(sys.stdin.readline())
postfix = sys.stdin.readline().strip()
numDict = dict()
for i in range(n):
    numDict[chr(65 + i)] = sys.stdin.readline().strip()

operator = '+-*/'
numStack = deque(list())

for i in postfix:
    if i in numDict.keys():
        numStack.append(numDict[i])
    elif i in operator:
        if len(numStack) >= 2:
            y = numStack.pop()
            x = numStack.pop()
            numStack.append(str(eval(x + i + y)))

answer = "%0.2f" % float(numStack[0])
print(answer)
