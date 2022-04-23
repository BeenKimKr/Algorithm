import sys

N = int(input())
words = list(set(sys.stdin.readline().strip() for _ in range(N)))
words.sort(key=lambda x: (len(x), x))
# sort() 2회가 더 빠름(각 116ms, 104ms)
# words.sort()
# words.sort(key=lambda x: len(x))

for i in words:
    print(i)
