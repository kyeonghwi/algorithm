import heapq
import sys

input = sys.stdin.readline

V, e = map(int,input().split())
k = int(input())

graph=[[] for _ in range(V+1)]
distance = [int(1e9)] * (V+1)
for _ in range(e):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))

def dijkstra(start):
    q =[]
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for next, next_cost in graph[now]:
            cost = dist + next_cost
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q,(cost, next))

dijkstra(k)

for i in range(1,V+1):
    if distance[i]==1e9:
        print("INF")
    else:
        print(distance[i])