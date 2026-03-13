T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    core=[]
    max_core = -1
    min_wire = 10000
    min_length = float('inf')
    direction =[(-1,0),(0,1),(1,0),(0,-1)]

    for i in range(n):
        for j in range(n):
            if arr[i][j] ==1:
                if i == 0 or j== 0 or i == n-1 or j == n-1:
                    continue
                core.append((i, j))

    def valid(x,y,dx,dy):
        path=[]
        nx, ny = x+ dx, y+dy
        while 0<=nx < n and 0<= ny < n:
            if arr[nx][ny] !=0:
                return None
            path.append((nx,ny))
            nx +=dx
            ny +=dy
        return path

    def dfs(idx, connected, total):
        global max_core, min_length

        if idx == len(core):
            if connected > max_core:
                max_core = connected
                min_length = total
            elif connected == max_core and total < min_length:
                if total < min_length:
                    min_length = total
            return

        dfs(idx+1, connected, total)

        x,y = core[idx]
        for dx,dy in direction:
            path = valid(x,y,dx,dy)
            if not path:
                continue

            for (px,py) in path:
                arr[px][py] = 2

            dfs(idx+1, connected+1, total+len(path))
            for (px,py) in path:
                arr[px][py] = 0

    dfs(0,0,0)
    print(f"#{tc} {min_length}")