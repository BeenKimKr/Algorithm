import sys
from collections import deque

n = int(sys.stdin.readline())
postfix = sys.stdin.readline().strip()
numDict = dict()
for i in range(n):
    numDict[chr(65 + i)] = sys.stdin.readline().strip()

operator = '+-*/'
numQueue = deque(list())

for i in postfix:
    if i in numDict.keys():
        numQueue.append(numDict[i])
    elif i in operator:
        if len(numQueue) >= 2:
            y = numQueue.pop()
            x = numQueue.pop()
            numQueue.append(str(eval(x + i + y)))

answer = "%0.2f" % float(numQueue[0])
print(answer)
