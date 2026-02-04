import sys

input = lambda: sys.stdin.readline().rstrip()
zeros = []


def check_row(r, num):
    for c in range(9):
        if arr[r][c] == num:
            return False
    return True


def check_col(c, num):
    for r in range(9):
        if arr[r][c] == num:
            return False
    return True


def check_square(r, c, num):
    nr = (r // 3) * 3
    nc = (c // 3) * 3
    for i in range(3):
        for j in range(3):
            if arr[nr + i][nc + j] == num:
                return False
    return True


def dfs(depth):
    if depth == len(zeros):
        for row in range(9):
            for col in range(9):
                print(arr[row][col], end="")
            print()
        exit()

    nr, nc = zeros[depth]
    for num in range(1, 10):
        if check_row(nr, num) and check_col(nc, num) and check_square(nr, nc, num):
            arr[nr][nc]=num
            dfs(depth+1)
            arr[nr][nc] = 0

arr=[]
for i in range(9):
    arr.append(list(map(int, input())))
    for j in range(9):
        if arr[i][j] ==0:
            zeros.append((i,j))
dfs(0)