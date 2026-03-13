import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

dp = [[0]*m for _ in range(n)]
visited = [[0]*m for _ in range(n)]

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def dfs(x,y):
    if dp[x][y]:      # 이미 계산된 칸이면 바로 반환
        return dp[x][y]

    if visited[x][y]: # 무한 루프 감지
        print(-1)
        exit()

    visited[x][y] = 1 # 현재 칸 방문 표시
    max_move = 1
    k = int(board[x][y]) # 이동해야 하는 거리
    for dx,dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx,ny = x+dx*k, y+dy*k
        if not in_range(nx,ny): # 보드 범위 밖
            continue
        if board[nx][ny] == "H": # 구멍
            continue
        max_move = max(max_move, dfs(nx,ny)+1) # 이동 횟수 업데이트

    visited[x][y] = 0 # 백트래킹: 현재 칸 방문 해제
    dp[x][y] = max_move # 현재 칸까지의 최대 이동 횟수
    return dp[x][y]

print(dfs(0,0))
