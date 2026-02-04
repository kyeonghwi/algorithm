import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
m = int(input())
com=[[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    com[a].append(b)
    com[b].append(a)
visited = set()
def bfs(start):
    queue = deque([start])
    visited.add(start)

    while queue:
        current = queue.popleft()
        for neighbor in com[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
bfs(1)
print(len(visited)-1)