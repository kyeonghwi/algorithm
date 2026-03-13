import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
T = int(input())
def in_range(x,y):
    return 0<=x<m and 0<=y<n

def dfs(x,y):
    arr[y][x]=0
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for dx,dy in direction:
        nx = x+dx
        ny = y + dy

        if in_range(nx,ny) and arr[ny][nx] ==1:
            dfs(nx,ny)

for tc in range(T):
    m,n,k = map(int,input().split())
    arr= [[0]* m for _ in range(n)]
    for _ in range(k):
        x,y = map(int,input().split())
        arr[y][x] = 1

    cnt=0
    for a in range(n):
        for b in range(m):
            if arr[a][b]==1:
                dfs(b,a)
                cnt+=1
    print(cnt)