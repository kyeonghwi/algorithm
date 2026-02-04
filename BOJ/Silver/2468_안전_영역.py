import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
arr= [list(map(int,input().split())) for _ in range(n)]
height =0
max_drown = 0
for i in range(n):
    for j in range(n):
        height= max(height, arr[i][j])

dx = [0 ,0, 1, -1]
dy = [1, -1, 0 ,0]

def bfs(a, b, value, visited):
    q = deque()
    q.append((a,b))
    visited[a][b] = 1

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<= ny <n:
                if arr[nx][ny] > value and visited[nx][ny] == 0:
                    visited[nx][ny] =1
                    q.append((nx,ny))

result = 0
for i in range(height):
    visited = [[0]*n for _ in range(n)]
    cnt = 0

    for j in range(n):
        for k in range(n):
            if arr[j][k] > i and visited[j][k] ==0:
                bfs(j,k,i,visited)
                cnt+=1
    if result < cnt:
        result = cnt
print(result)