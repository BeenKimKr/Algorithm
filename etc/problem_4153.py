while True:
    edge = list(map(int, input().split()))
    if edge == [0, 0, 0]:
        break
    edge.sort()
    print('right') if edge[0]**2 + edge[1]**2 == edge[2]**2 else print('wrong')
