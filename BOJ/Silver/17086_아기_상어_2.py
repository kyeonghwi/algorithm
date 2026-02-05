from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
queue =deque()
dist = [[-1] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] ==1:
            queue.append((i,j))
            dist[i][j]=0

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

while queue:
    x,y = queue.popleft()

    for i in range(8):
        nx,ny=x+dx[i],y+dy[i]
        if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            queue.append((nx, ny))

safe_dist=0
for i in range(n):
    for j in range(m):
         safe_dist = max(safe_dist,dist[i][j])
print(safe_dist)