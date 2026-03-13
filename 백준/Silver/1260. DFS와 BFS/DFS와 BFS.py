import sys
from collections import deque

input = sys.stdin.readline
n, m, v = map(int,input().split())
graph=[[] for _ in range(n+1)]
for i in range(m):
    a, b= map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for elem in graph:
    elem.sort()
def dfs(v, visited):
    visited[v] = True
    print(v,end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(i,visited)

def bfs(start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
visited = [False]*(n+1)
visited_b = [False]*(n+1)
dfs(v, visited)
print()
bfs(v, visited_b)
