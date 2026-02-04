import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int,input().split())
arr = [list(map(int,input().strip())) for _ in range(n)]

def in_range(y,x):
    return 0<=x<m and 0<=y<n

visited = [[False]*m for _ in range(n)]
queue = deque()
queue.append((0,0,1))
visited[0][0] = True

dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]

while queue:
    y,x,dist = queue.popleft()
    if y==n-1 and x == m-1:
        print(dist)
        break
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if in_range(ny,nx) and not visited[ny][nx] and arr[ny][nx]==1:
            visited[ny][nx] = True
            queue.append((ny,nx,dist+1))