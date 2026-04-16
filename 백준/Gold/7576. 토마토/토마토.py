from collections import deque

def bfs(N, M):
    q= deque()
    visited = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if tomato[i][j] ==1:
                q.append((i,j))
                visited[i][j] =1
    while q:
        i ,j = q.popleft()
        tomato[i][j] = 1
        for di,dj in [[0,1], [0,-1], [1,0], [-1,0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<M:
                if tomato[ni][nj] ==0 and visited[ni][nj]==0:
                    q.append((ni, nj))
                    visited[ni][nj] = visited[i][j] + 1

    max_v =0
    for i in range(N):
        for j in range(M):
            if tomato[i][j]==0:
                return -1
            elif max_v < visited[i][j]:
                max_v = visited[i][j]
    return max_v -1
M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]

ans = bfs(N, M)
print(ans)