import sys
from collections import deque

input = sys.stdin.readline
m,n,h = map(int,input().split())
arr=[]
for i in range(h):
    floor = [list(map(int,input().split())) for _ in range(n)]
    arr.append(floor)

def in_range(x,y,z):
    return 0<=x<n and 0<=y<m and 0<=z<h

direction = ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,-1),(0,0,1))
queue = deque()

def bfs():
    while queue:
        z,x,y = queue.popleft()
        for i in range(6):
            nx, ny, nz = x + direction[i][0], y + direction[i][1], z + direction[i][2]
            if in_range(nx,ny,nz):
                if arr[nz][nx][ny] == 0:
                    arr[nz][nx][ny] = arr[z][x][y] + 1
                    queue.append((nz,nx,ny))

for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] ==1:
                queue.append((i,j,k))
bfs()

complete = True
day = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] ==0:
                complete = False
            day = max(day, arr[i][j][k])
if not complete:
    print(-1)
else:
    print(day-1)