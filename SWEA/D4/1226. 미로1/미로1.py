def dfs(i, j):
    global ans
    if maze[i][j] == '3':
        ans = 1
    visited[i][j] = 1
    for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
        ni, nj = i+ di, i+dj
        if 0<=ni<16 and 0<=nj<16:
            if maze[ni][nj] != '1' and visited[ni][nj]==0:
                dfs(ni, nj)

def find_start():
    for i in range(16):
        for j in range(16):
            if maze[i][j] == '2':
                return i, j

T = 10
for _ in range(T):
    tc = int(input())
    maze = [input() for _ in range(16)]
    visited = [[0]*16 for _ in range(16)]

    sti, stj = find_start()

    ans = 0
    dfs(sti,stj)
    print(f'#{tc} {ans}')