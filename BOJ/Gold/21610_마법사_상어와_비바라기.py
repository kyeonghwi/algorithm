import sys

input = sys.stdin.readline

n,m=map(int,input().split())

def in_range(x,y):
    return 0<=x<n and 0<=y<n
basket= [list(map(int,input().split())) for _ in range(n)]

dx=[0,-1,-1,-1,0,1,1,1]
dy=[-1,-1,0,1,1,1,0,-1]
# 대각선 1,3,5,7 

cloud = [(n-1,0),(n-1,1),(n-2,0),(n-2,1)]
for _ in range(m):
    temp_cloud=[]
    d,s = map(int,input().split())
    while cloud:
        x,y= cloud.pop()
        nx,ny = (x+dx[d-1]*s)%n, (y+dy[d-1]*s)%n
        temp_cloud.append((nx,ny))
        basket[nx][ny] +=1
    for nx,ny in temp_cloud:
        cnt=0
        for i in range(1,8,2):
            a, b = nx+dx[i], ny+dy[i]
            if in_range(a,b) and basket[a][b]>0:
                cnt+=1
        basket[nx][ny]+=cnt
    prev_cloud_pos = set(temp_cloud)
    for newx in range(n):
        for newy in range(n):
            if basket[newx][newy] >=2 and (newx,newy) not in prev_cloud_pos:
                cloud.append((newx,newy))
                basket[newx][newy] -=2
total=0
for row in basket:
    total +=sum(row)
print(total)