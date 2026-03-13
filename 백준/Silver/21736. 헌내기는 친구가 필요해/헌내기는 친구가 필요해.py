import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int,input().split())
arr = [list(input().strip()) for _ in range(n)]
start_x, start_y = -1,-1
for i in range(n):
    for j in range(m):
        if arr[i][j]=="I":
            start_x = i
            start_y = j
            break
    if start_x != -1:
        break

def in_range(x,y):
    return 0<=x<n and 0<=y<m

visited = [[False]*m for _ in range(n)]
queue = deque()
queue.append((start_x,start_y))
visited[start_x][start_y] = True

cnt=0
while queue:
    x, y = queue.popleft()
    direction = ((1,0),(-1,0),(0,-1),(0,1))
    for dx, dy in direction:
        nx, ny = x + dx, y +dy
        if in_range(nx,ny) and not visited[nx][ny]:
            if arr[nx][ny] =="O":
                visited[nx][ny] = True
                queue.append((nx,ny))
            elif arr[nx][ny] =="P":
                cnt+=1
                visited[nx][ny] = True
                queue.append((nx,ny))
if cnt!=0:
    print(cnt)
else:
    print("TT")