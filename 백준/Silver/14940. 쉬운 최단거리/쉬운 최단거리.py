import sys
from collections import deque

input = sys.stdin.readline
n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

answer = [[-1] * m for _ in range(n)]
start_x, start_y = -1, -1

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            start_x, start_y = i, j
            answer[i][j] = 0
        elif arr[i][j] == 0:
            answer[i][j] = 0

def in_range(x,y):
    return 0<=x<n and 0<=y<m
def bfs(x,y):
    q = deque()
    q.append((x,y))
    direction = ((1,0),(-1,0),(0,1),(0,-1))

    while q:
        curr_x,curr_y = q.popleft()
        for dx,dy in direction:
            nx, ny = curr_x+dx, curr_y+dy
            if in_range(nx,ny) and answer[nx][ny]==-1:
                answer[nx][ny] = answer[curr_x][curr_y] +1
                q.append((nx,ny))

bfs(start_x,start_y)
for i in range(n):
    for j in range(m):
        print(answer[i][j], end=" ")
    print()