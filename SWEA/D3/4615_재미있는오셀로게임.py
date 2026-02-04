T = int(input())
for tc in range(1, T + 1):
    n, m = map(int,input().split())

    arr= [[0]*n for _ in range(n)]
    arr[n//2-1][n//2-1], arr[n//2][n//2] = 2,2
    arr[n//2-1][n//2], arr[n//2][n//2-1] = 1,1

    def in_range(x,y):
        return 0<=x<n and 0<=y <n

    direc = [(0,-1),(0,1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
    for _ in range(m):
        y, x, c = map(int,input().split())
        y -=1
        x-=1
        arr[x][y] = c
        for dx, dy in direc:
            nx, ny = x + dx, y + dy
            flip = []
            while in_range(nx, ny) and arr[nx][ny] != 0 and arr[nx][ny] != c:
                flip.append((nx, ny))
                nx += dx
                ny += dy
            if in_range(nx, ny) and arr[nx][ny] == c:
                for fx, fy in flip:
                    arr[fx][fy] = c
    w=0
    b=0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                b += 1
            elif arr[i][j] == 2:
                w += 1
    print(f"#{tc} {b} {w}")
