T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(input().strip()) for _ in range(n)]

    min_click= n*n
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1), (0, 1),
                  (1, -1), (1, 0), (1, 1)]

    def around(x,y):
        cnt=0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0<=nx<n and 0<=ny<n:
                if arr[nx][ny] =="*":
                    cnt+=1
        return cnt
    def num(x,y):
        if arr[x][y] != ".":
            return
        mine=0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0<=nx<n and 0<=ny<n:
                if arr[nx][ny] =="*":
                    mine+=1
            arr[x][y] = str(mine)
        if mine==0:
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    num(nx,ny)

    def dfs(idx, click):
        global min_click
        if idx ==n*n:
            if min_click > click:
                min_click = click
            return
        for i in range(n*n):
            if arr[idx//n][idx%n]=="." and  around(idx//n, idx%n)==0:
                num(idx // n, idx % n)
                dfs(idx+1, click+1)
                break

        if arr[idx//n][idx%n] =="*" or arr[idx//n][idx%n] in set("012345678"):
            dfs(idx+1, click)
        elif arr[idx//n][idx%n] ==".":
            num(idx//n,idx%n)
            dfs(idx+1, click+1)

    count=0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == "." and around(i,j)==0:
                num(i,j)
                count+=1
    for i in range(n):
        for j in range(n):
            if arr[i][j] == ".":
                count+=1
    print(f"#{tc} {count}")