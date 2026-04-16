def dfs(i, j ,N, k):
    global cnt
    cnt +=1
    visited[i][j] = k
    for di, dj in [[0,1],[1,0],[-1,0],[0,-1]]:
        ni, nj = i+ di, j+dj
        if 0<=ni<N and 0<=nj<N:
            if arr[ni][nj]=='1' and visited[ni][nj]==0:
                dfs(ni, nj, N, k)

N = int(input())
arr = [input() for _ in range(N)]

ans = []
visited = [[0]*N for _ in range(N)]

k = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == '1' and visited[i][j]==0:
            k += 1 # 개 단지번호
            cnt = 0 # 단지내 가구 수
            dfs(i, j ,N ,k)
            ans.append(cnt)
ans.sort()
print(k)
for x in ans:
    print(x)