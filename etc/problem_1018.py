import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
board = list(sys.stdin.readline().strip() for _ in range(n))
w_start = ['WBWBWBWB',
           'BWBWBWBW',
           'WBWBWBWB',
           'BWBWBWBW',
           'WBWBWBWB',
           'BWBWBWBW',
           'WBWBWBWB',
           'BWBWBWBW']
b_start = ['BWBWBWBW',
           'WBWBWBWB',
           'BWBWBWBW',
           'WBWBWBWB',
           'BWBWBWBW',
           'WBWBWBWB',
           'BWBWBWBW',
           'WBWBWBWB']
check_min = 64
check_w = 0
check_b = 0

"""
4중 for문 => 바깥 2중 for문은 8 * 8의 인덱스를, 안쪽 2중 for문은 입력한 보드의 8 * 8의 인덱스를 가져옴.
8*8씩 2중리스트로 접근해야 하나? 반복을 두 번 돌아야 하나? 등의 생각이 들어 뭔가 어렵게 느껴졌다...
무식하게 구현했지만 solve 후에 보니 복잡한 듯 보여도 간단한 로직.
"""
for i in range(n-7):
    for j in range(m-7):
        check_w = 0
        check_b = 0
        for x in range(i, i+8):
            for y in range(j, j+8):
                if board[x][y] != w_start[x-i][y-j]:
                    check_w += 1
                if board[x][y] != b_start[x-i][y-j]:
                    check_b += 1
        check_min = min(check_min, min(check_w, check_b))

print(check_min)
