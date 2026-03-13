import sys

input = sys.stdin.readline
n, m = map(int,input().split())

s =[]
visited= [False] * (n+1)
def dfs():
    if len(s)==m:
        print(*s)
        return

    for i in range(1,n+1):
        if not visited[i]:
            if not s or (s and s[-1] <= i):
                s.append(i)
                visited[i] = True
                dfs()
                s.pop()
                visited[i] = False
dfs()