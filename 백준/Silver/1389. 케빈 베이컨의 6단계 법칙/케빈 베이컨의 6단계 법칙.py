import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int,input().split())
friend = [[] for _ in range(n+1)]
for _ in range(m):
    a, b =map(int,input().split())
    friend[a].append(b)
    friend[b].append(a)

def bfs(start):
    distance= [-1] * (n+1)
    queue = deque()
    queue.append(start)
    distance[start] = 0

    while queue:
        current = queue.popleft()
        for neighbor in friend[current]:
            if distance[neighbor] == -1:
                distance[neighbor] = distance[current] +1
                queue.append(neighbor)
    return sum(distance[1:])
min_bacon = float('inf')
result_person=0
for i in range(1,n+1):
    current_bacon = bfs(i)

    if current_bacon < min_bacon:
        min_bacon = current_bacon
        result_person = i

print(result_person)