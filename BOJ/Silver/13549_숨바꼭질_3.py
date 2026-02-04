import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int,input().split())

visited=[1e9]*100001
queue = deque()
queue.append((n,0))
visited[n] = 0

while queue:
    x, t = queue.popleft()
    if x==k:
        print(t)
        break
    if 0<=x*2< 100001 and visited[x*2] >t:
        visited[x*2] = t
        queue.appendleft((x*2,t))
    for nx in(x-1,x+1):
        if 0<= nx < 100001 and visited[nx] > t+1:
            visited[nx] = t+1
            queue.append((nx,t+1))