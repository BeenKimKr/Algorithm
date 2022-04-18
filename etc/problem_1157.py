word = input().upper()
wordDict = dict()

for i in word:
    if i in wordDict.keys():
        wordDict[i] += 1
    else:
        wordDict[i] = 1

wordDict = sorted(wordDict.items(), key=lambda x: x[1], reverse=True)

if len(wordDict) == 1:
    result = wordDict[0][0]
else:
    result = '?' if wordDict[0][1] == wordDict[1][1] else wordDict[0][0]

print(result)
