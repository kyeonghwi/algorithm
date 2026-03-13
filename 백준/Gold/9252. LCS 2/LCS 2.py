import sys

input = lambda: sys.stdin.readline().rstrip()
arr1 = list(input())
arr2 = list(input())

dp=[['' for _ in range(len(arr2)+1)] for _ in range(len(arr1)+1)]

for i in range(1, len(arr1)+1):
   for j in range(1,len(arr2)+1):
       if arr1[i-1] == arr2[j-1]:
           dp[i][j]= dp[i-1][j-1] + arr1[i-1]
       else:
           dp[i][j] = dp[i - 1][j] if len(dp[i - 1][j]) > len(dp[i][j - 1]) else dp[i][j - 1]

print(len(dp[len(arr1)][len(arr2)]))
print(dp[len(arr1)][len(arr2)])