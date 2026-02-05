import sys

input = sys.stdin.readline
n= int(input())
arr=[list(map(int,input().split())) for _ in range(n)]

legin = 0
for i in range(n):
    for j in range(n):
        if arr[i][j]==2:
            if (i+j)%2==0:
                legin=0
            else:
                legin=1

result=True
for i in range(n):
    for j in range(n):
        if arr[i][j]==1:
            if (i+j)%2!=legin:
                continue
            else:
                result = False
                break
    if not result:
        break

if result:
    print("Lena")
else:
    print("Kiriya")