import sys
from collections import deque

INF = 1e+9
n = int(input())
mat = []
for i in range(n):
    mat.append(list(map(int, sys.stdin.readline().split())))
    
dp = [[INF for _ in range(1<<n)] for _ in range(n)]    #모든 방문 가능 경우의 수
chk = 1


dp[0][chk]=0
queue = deque([[0, chk]])
answer = [INF for _ in range(n)]
while queue:
    node, chk = queue.popleft()
    if chk==(1<<n)-1:
        if mat[node][0]!=0:
            answer[node] = dp[node][chk] + mat[node][0]
        else:
            dp[node][chk] = INF
    else:
        for i in range(1, n):
            if (mat[node][i]!= 0)and ((chk & (1<<i))==0):    #연결되어 있으며 방문한적 없을때
                if dp[node][chk] + mat[node][i] < dp[i][chk | (1<<i)]:
                    dp[i][chk | (1<<i)] = dp[node][chk] + mat[node][i]
                    queue.append([i, chk | (1<<i)])

answer = min(answer)
print(answer)