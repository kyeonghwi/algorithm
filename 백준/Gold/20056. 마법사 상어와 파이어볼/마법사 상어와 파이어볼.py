from collections import deque
import sys

input = sys.stdin.readline

N,M,K=map(int,input().split())

dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,1,1,1,0,-1,-1,-1]

board = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    board[r - 1][c - 1].append([m, s, d])

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(K):
    next_board = [[[] for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            for m, s, d in board[r][c]:
                nr = (r + dx[d] * s) % N
                nc = (c + dy[d] * s) % N
                next_board[nr][nc].append([m, s, d])
    
    board = next_board

    for r in range(N):
        for c in range(N):
            if len(board[r][c]) >= 2:
                sum_m, sum_s, cnt = 0, 0, len(board[r][c])
                is_all_odd_or_even = True
                first_dir_type = board[r][c][0][2] % 2

                for m, s, d in board[r][c]:
                    sum_m += m
                    sum_s += s
                    if d % 2 != first_dir_type:
                        is_all_odd_or_even = False

                new_m = sum_m // 5
                new_s = sum_s // cnt
                
                board[r][c] = []

                if new_m > 0:
                    if is_all_odd_or_even:
                        new_dirs = [0, 2, 4, 6]
                    else:
                        new_dirs = [1, 3, 5, 7]
                    
                    for nd in new_dirs:
                        board[r][c].append([new_m, new_s, nd])

total_mass = 0
for r in range(N):
    for c in range(N):
        for m, s, d in board[r][c]:
            total_mass += m

print(total_mass)