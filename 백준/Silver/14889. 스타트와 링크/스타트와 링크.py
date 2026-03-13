import sys

input = sys.stdin.readline
n = int(input())
arr= [list(map(int,input().split())) for _ in range(n)]

team = [[0]for _ in range(2)]
diff = 1e9
visited = [False for _ in range(n)]
def dfs(cnt, idx):
    global diff
    if cnt==n//2:
        A = 0
        B = 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    A += arr[i][j]
                elif not visited[i] and not visited[j]:
                    B += arr[i][j]
        diff = min(diff, abs(A - B))

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(cnt + 1, i + 1)
            visited[i] = False
dfs(0, 0)
print(diff)