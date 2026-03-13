import sys

input = sys.stdin.readline
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

min_dp = arr[0][:]
max_dp=arr[0][:]

for i in range(1,n):
    a,b,c= arr[i]
    max0 = max(max_dp[0], max_dp[1]) + a
    max1= max(max_dp)+b
    max2 = max(max_dp[1], max_dp[2]) +c

    min0 = min(min_dp[0], min_dp[1]) + a
    min1 = min(min_dp) + b
    min2 = min(min_dp[1], min_dp[2]) + c

    max_dp= [max0,max1,max2]
    min_dp = [min0,min1,min2]
print(max(max_dp), min(min_dp))


# min_score= 900000
# max_score = 0
# def dfs(depth, score, pos):
#     global max_score
#     global min_score
#     if depth ==3:
#         max_score = max(score, max_score)
#         min_score = min(score, min_score)
#         return
#     for i in range(-1,2,1):
#         new_pos = pos+i
#         if 0<=new_pos<3:
#             dfs(depth+1,score+arr[depth][new_pos],new_pos)
#
# for i in range(3):
#     dfs(0,0,i)
# print(max_score, min_score)