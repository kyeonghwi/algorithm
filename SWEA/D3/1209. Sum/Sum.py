T = 10
for tc in range(1, T+1):
    n= int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    result=[]
    for i in range(100):
        row = sum(arr[i])
        result.append(row)
    for j in range(100):
        col = sum(arr[i][j] for i in range(100))
        result.append(col)

    diag1 = sum(arr[i][i] for i in range(100))
    diag2 = sum(arr[99-i][i] for i in range(100))
    result.append(diag1)
    result.append(diag2)
    print(f"#{tc} {max(result)}")
