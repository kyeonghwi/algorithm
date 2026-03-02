import sys
import copy
sys.setrecursionlimit(100000)

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
max_block = 0

def move(board, direction):
    N = len(board)
    new_board = [[0]*N for _ in range(N)]
    merged = [[False]*N for _ in range(N)]

    if direction == 0:  # 위로 이동
        for j in range(N):
            index = 0
            for i in range(N):
                if board[i][j]:
                    temp = board[i][j]
                    board[i][j] = 0
                    if new_board[index][j] == 0:
                        new_board[index][j] = temp
                    elif new_board[index][j] == temp and not merged[index][j]:
                        new_board[index][j] *= 2
                        merged[index][j] = True
                        index += 1
                    else:
                        index += 1
                        new_board[index][j] = temp
    elif direction == 1:  # 아래로 이동
        for j in range(N):
            index = N - 1
            for i in range(N-1, -1, -1):
                if board[i][j]:
                    temp = board[i][j]
                    board[i][j] = 0
                    if new_board[index][j] == 0:
                        new_board[index][j] = temp
                    elif new_board[index][j] == temp and not merged[index][j]:
                        new_board[index][j] *= 2
                        merged[index][j] = True
                        index -= 1
                    else:
                        index -= 1
                        new_board[index][j] = temp
    elif direction == 2:  # 왼쪽으로 이동
        for i in range(N):
            index = 0
            for j in range(N):
                if board[i][j]:
                    temp = board[i][j]
                    board[i][j] = 0
                    if new_board[i][index] == 0:
                        new_board[i][index] = temp
                    elif new_board[i][index] == temp and not merged[i][index]:
                        new_board[i][index] *= 2
                        merged[i][index] = True
                        index += 1
                    else:
                        index += 1
                        new_board[i][index] = temp
    else:  # 오른쪽으로 이동
        for i in range(N):
            index = N - 1
            for j in range(N-1, -1, -1):
                if board[i][j]:
                    temp = board[i][j]
                    board[i][j] = 0
                    if new_board[i][index] == 0:
                        new_board[i][index] = temp
                    elif new_board[i][index] == temp and not merged[i][index]:
                        new_board[i][index] *= 2
                        merged[i][index] = True
                        index -= 1
                    else:
                        index -= 1
                        new_board[i][index] = temp
    return new_board

def dfs(board, depth):
    global max_block
    if depth == 5:
        for i in range(N):
            max_block = max(max_block, max(board[i]))
        return
    for i in range(4):
        new_board = move(copy.deepcopy(board), i)
        dfs(new_board, depth + 1)

dfs(board, 0)
print(max_block)
출처: https://dev-guardy.tistory.com/104 [Developer Guardy:티스토리]
