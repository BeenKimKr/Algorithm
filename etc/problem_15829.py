L = int(input())
word = input()
table = {chr(ord('a')+i): i+1 for i in range(26)}
result = 0

for i in range(L):
    result += table[word[i]] * (31**i)

result %= 1234567891
print(result)
