import sys

input = sys.stdin.readline
n, m = map(int,input().split())
arr = [list(input().strip()) for _ in range(n)]

x,y=0,0
for i in range(n):
    if "X" in arr[i]:
        continue
    else:
        x+=1
for i in range(m):
    found = False
    for j in range(n):
        if arr[j][i]=="X":
            found = True
            break
    if not found:
        y+=1
print(max(x,y))