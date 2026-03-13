import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int,input().split())
move = {}
for _ in range(n+m):
    x,y = map(int,input().split())
    move[x] =y

dist=[-1]*101
queue=deque()
queue.append(1)
dist[1] = 0
while queue:
    pos = queue.popleft()
    for dice in range(1,7):
        next_pos = pos + dice

        if next_pos > 100:
            continue
        if next_pos in move:
            end_pos = move[next_pos]
        else:
            end_pos = next_pos
        if dist[end_pos] ==-1:
            dist[end_pos] = dist[pos]+1
            queue.append(end_pos)
print(dist[100])