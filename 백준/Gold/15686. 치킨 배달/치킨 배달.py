import sys
from itertools import combinations

input = sys.stdin.readline
n, m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

chicken = []
house=[]
for i in range(n):
    for j in range(n):
        if arr[i][j]==2:
            chicken.append((i,j))
        if arr[i][j]==1:
            house.append((i,j))

ans=1e9
for comb in combinations(chicken,m):
    total =0
    for x1,y1 in house:
        dist = 1e9
        for x2, y2 in comb:
            dist = min(dist, abs(x1-x2)+abs(y1-y2))
        total += dist
    ans = min(total, ans)
print(ans)