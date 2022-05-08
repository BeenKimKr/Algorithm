import math
a, b, v = map(int, input().split())
work = a - b
day = (v-b-1) // (a-b) + 1
print(day)
