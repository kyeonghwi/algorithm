T= int(input())
for tc in range(1,T+1):
    n,m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    maxv = 0
    for i in range(n-m+1):
        for j in range(n - m + 1):
            value = 0
            for a in range(m):
                for b in range(m):
                    value += arr[i+a][j+b]
            maxv = max(maxv,value)
    print(f"#{tc} {maxv}")