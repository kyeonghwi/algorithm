import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
arr= [list(input().strip()) for _ in range(n)]

direc = [(1,0),(-1,0),(0,-1),(0,1)]
rgb=[[False]*n for _ in range(n)]
normal =[[False]*n for _ in range(n)]
rgb_cnt, normal_cnt = 0,0
def bfs_normal(x,y):
    color = arr[x][y]
    queue = deque()
    queue.append((x,y))
    normal[x][y] = True

    while queue:
        i,j = queue.popleft()
        for dx,dy in direc:
            nx,ny= i + dx, j+dy
            if 0<=nx<n and 0<=ny<n and not normal[nx][ny]:
                if arr[nx][ny] == color:
                    normal[nx][ny] = True
                    queue.append((nx,ny))

def bfs_rgb(x,y):
    color = arr[x][y]
    queue = deque()
    queue.append((x,y))
    rgb[x][y] = True

    while queue:
        i,j = queue.popleft()
        for dx,dy in direc:
            nx,ny= i + dx, j+dy
            if 0<=nx<n and 0<=ny<n and not rgb[nx][ny]:
                if color in ('R', "G") and arr[nx][ny] in ('R', "G"):
                    rgb[nx][ny] = True
                    queue.append((nx,ny))
                elif color == arr[nx][ny]=="B":
                    rgb[nx][ny] = True
                    queue.append((nx,ny))


for i in range(n):
    for j in range(n):
        if not normal[i][j]:
            bfs_normal(i,j)
            normal_cnt+=1
for i in range(n):
    for j in range(n):
        if not rgb[i][j]:
            bfs_rgb(i,j)
            rgb_cnt +=1
print(normal_cnt, rgb_cnt)