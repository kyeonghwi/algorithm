import sys

input = sys.stdin.readline
n, m = map(int,input().split())
sq=[]
visited= [False] * (n+1)
def dfs(graph):
    if len(graph)== m:
        print(" ".join(graph))
        return
    for i in range(1,n+1):
        if not visited[i]:
            visited[i] = True
            graph.append(str(i))
            dfs(graph)
            graph.pop()
            visited[i] = False
dfs(sq)