import sys

input = sys.stdin.readline
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]\

dp = [0] * (n+1)
for i in range(n-1, -1,-1):
    time = arr[i][0]
    price = arr[i][1]

    if i + time > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], price + dp[i+ time])
print(dp[0])