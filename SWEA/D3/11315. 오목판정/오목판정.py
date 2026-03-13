T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(str,input().strip())) for _ in range(n)]

    stone = False
    def in_range(x,y):
        return 0<=x<n and 0<= y <n

    for i in range(n):
        for j in range(n-4):
            if not "." in arr[i][j:j+5]:
                stone = True
                break
            if all(arr[j+a][i]=="o" for a in range(5)):
                stone = True
                break
        if stone:
            break
    directions = [(1,1),(-1,-1),(1,-1),(-1,1)]
    for i in range(n):
        for j in range(n):
            for dx,dy in directions:
                nx, ny = i,j
                cnt =0
                while in_range(nx,ny) and arr[nx][ny]=="o" and cnt<5:
                    nx, ny = nx + dx, ny + dy
                    cnt+=1
                if cnt==5:
                    stone = True
                    break
            if stone:
                break
        if stone:
            break
    if stone:
        print(f"#{tc} {'YES'}")
    else:
        print(f"#{tc} {'NO'}")
