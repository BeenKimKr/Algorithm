input()
std = sorted(list(map(int, input().split())))
input()
comp = input().split()

for c in comp:
    i = int(c)
    start = 0
    end = len(std) - 1

    while start <= end:
        mid = (start + end) // 2
        if std[mid] < i:
            start = mid + 1
        elif std[mid] > i:
            end = mid - 1
        elif std[mid] == i:
            print(1)
            break
        else:
            print(0)
            break

        if start > end:
            print(0)
            break
