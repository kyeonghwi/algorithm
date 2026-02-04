import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
arr = list(map(int,input().split()))
m=int(input())

dp = [[0] * n for _ in range(n)]

for i in range(n):
    dp[i][i]=1

for i in range(n-1):
    if arr[i] ==arr[i+1]:
        dp[i][i+1]=1

for i in range(3,n+1):
    for j in range(n- i +1):
        e = j+ i -1
        if arr[j] == arr[e] and dp[j+1][e-1]==1:
            dp[j][e]=1

for _ in range(m):
    s,e= map(int,input().split())
    print(dp[s-1][e-1])