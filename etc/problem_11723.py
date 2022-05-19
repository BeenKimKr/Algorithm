from sys import stdin

M = int(stdin.readline().strip())
S = set()

for _ in range(M):
    line = stdin.readline().strip()

    if line == 'all':
        S = set(range(1, 21))
    elif line == 'empty':
        S.clear()
    else:
        order = line.split()[0]
        x = int(line.split()[1])

        if order == 'add':
            if x in S:
                continue
            S.add(x)
        elif order == 'remove':
            S.discard(x)
        elif order == 'check':
            if x in S:
                print(1)
            else:
                print(0)
        else:
            if x in S:
                S.discard(x)
            else:
                S.add(x)
