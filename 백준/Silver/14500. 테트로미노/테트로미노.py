import sys

input = sys.stdin.readline
n, m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

max_v = 0
visited = [[False]*m for _ in range(n)]
def dfs(x,y, cnt, total):
    global max_v
    direc = [(1,0),(0,1),(-1,0),(0,-1)]

    if cnt==4:
        max_v = max(max_v, total)
        return

    for dx, dy in direc:
        nx, ny = x + dx, y+ dy
        if 0<=nx< n and 0<= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx,ny,cnt+1,total+board[nx][ny])
            visited[nx][ny] = False

def t(x,y):
    global max_v
    shapes = [
        [(0, 0), (0, 1), (0, 2), (1, 1)],
        [(0, 0), (1, 0), (2, 0), (1, 1)],
        [(0, 1), (1, 0), (1, 1), (1, 2)],
        [(0, 1), (1, 1), (2, 1), (1, 0)]
    ]

    for row in shapes:
        total = 0
        for dx,dy in row:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                total += board[nx][ny]

        max_v = max(max_v, total)
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i,j,0,0)
        visited[i][j] = False
        t(i,j)
print(max_v)