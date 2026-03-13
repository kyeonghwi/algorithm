T = 10
for tc in range(1, T+1):
    n= int(input())
    arr = [list(input().strip()) for _ in range(8)]
    def in_range(x,y):
        return 0<=x<8 and 0<=y<8
    pend=0

    for i in range(8):
        for j in range(8-n+1):
            if in_range(i,j+n-1):
                if all(arr[i][j+a]==arr[i][j+n-1-a] for a in range(n//2)):
                    pend+=1
    for j in range(8):
        for i in range(8-n+1):
            if in_range(i+n-1,j):
                if all(arr[i+a][j]==arr[i+n-1-a][j] for a in range(n//2)):
                    pend+=1
    print(f"#{tc} {pend}")