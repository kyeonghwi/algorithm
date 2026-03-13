T = int(input())
for tc in range(1, T+1):
    n= int(input())
    print(f"#{tc}")

    dx = [0, 1, 0, -1]  # 행 변화량: 우, 하, 좌, 상
    dy = [1, 0, -1, 0]  # 열 변화량: 우, 하, 좌, 상
    arr=[[0]*n for _ in range(n)]
    def in_range(x,y):
        return 0<=x<n and 0<=y<n

    a, b= 0,0
    index = 0
    arr[a][b] =1
    for i in range(2,n*n+1):
        x,y = a + dx[index], b+dy[index]
        if not in_range(x,y) or arr[x][y] !=0:
            index = (index+1)%4
        a,b = a + dx[index], b + dy[index]
        arr[a][b] = i
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=" ")
        print()
