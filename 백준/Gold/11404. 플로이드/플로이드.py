import sys

input = sys.stdin.readline

INF = 10 ** 9

n = int(input())
m = int(input())

dist = [[INF] * n for _ in range(n)]
for i in range(n):
    dist[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    if c < dist[a][b]:
        dist[a][b] = c

for k in range(n):
    for i in range(n):
        if dist[i][k] == INF:
            continue
        for j in range(n):
            if dist[k][j] == INF:
                continue
            new_cost = dist[i][k] + dist[k][j]
            if new_cost < dist[i][j]:
                dist[i][j] = new_cost

for row in dist:
    print(' '.join('0' if value == INF else str(value) for value in row))