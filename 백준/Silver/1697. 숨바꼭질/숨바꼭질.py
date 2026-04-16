from collections import deque

N, k =map(int, input().split())

q= deque()
visited = [0] * 100001
q.append(N)
visited[N] = 1
while q:
    t= q.popleft()
    if t == k:
        break

    if t-1 >= 0 and visited[t-1]==0:
        q.append(t-1)
        visited[t-1] = visited[t] + 1
    if t+1<=100000 and visited[t+1]==0:
        q.append(t+1)
        visited[t+1] = visited[t] + 1
    if 2*t<= 100000 and visited[2*t]==0:
        q.append(2*t)
        visited[2*t] = visited[t] + 1

print(visited[k] -1)