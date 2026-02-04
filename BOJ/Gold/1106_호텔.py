import sys
inf = float('inf')

input = lambda: sys.stdin.readline().rstrip()
c,n = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

total=0
dp=[inf] * (c+100)
dp[0]=0

for cost, man in arr:
    for i in range(man,c+100):
        if dp[i-man] != inf:
            dp[i] = min(dp[i],dp[i-man]+cost)
print(min(dp[c:]))