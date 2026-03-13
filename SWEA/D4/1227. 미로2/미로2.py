from collections import deque

def find_start():
    for i in range(100):
        for j in range(100):
            if maze[i][j] == '2':
                return i, j
def bfs(i, j):
    q = deque()
    visited = [[0]*100 for _ in range(100)]
    q.append((i,j))
    visited[i][j] = 1
    while q:
        i, j = q.popleft()
        if maze[i][j] =='3':
            return 1            #거리는 return visited[i][j]

        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < 100 and 0 <= nj < 100:
                if maze[ni][nj] != '1' and visited[ni][nj] == 0:
                    q.append((ni, nj))
                    visited[ni][nj] = visited[i][j] + 1
    return 0


T = 10
for _ in range(T):
    tc = int(input())

    maze = [input() for _ in range(100)]
    sti, stj= find_start()
    ans = bfs(sti, stj)
    print(f'#{tc} {ans}')