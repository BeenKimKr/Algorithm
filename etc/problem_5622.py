s = input()
d = {2: 'ABC', 3: 'DEF', 4: 'GHI', 5: 'JKL',
     6: 'MNO', 7: 'PQRS', 8: 'TUV', 9: 'WXYZ'}
t = 0

for i in s:
    for j in range(2, 10):
        if i in d[j]:
            t += (j+1)

print(t)
