T= int(input())
for tc in range(1, T+1):
    n = int(input())
    arr=[list(map(int,input().strip())) for _ in range(n)]

    harvest = 0
    k=0
    for i in range(n):
        harvest +=sum(arr[i][n//2-k:n//2+k+1])
        if i < n//2:
            k+=1
        else:
            k-=1
    print(f"#{tc} {harvest}")