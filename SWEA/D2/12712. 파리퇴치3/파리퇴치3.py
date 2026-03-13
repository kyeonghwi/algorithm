T = int(input())
for tc in range(1, T + 1):
    n,m = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    line=[]
    diagonal=[]

    for i in range(n):
        for j in range(n):
            temp = []
            for a in range(1,m):
                if i - a >= 0 and j - a >= 0:
                    temp.append(arr[i - a][j - a])
                if i + a < n and j + a < n:
                    temp.append(arr[i + a][j + a])
                if i + a < n and j - a >= 0:
                    temp.append(arr[i + a][j - a])
                if i - a >= 0 and j + a < n:
                    temp.append(arr[i - a][j + a])
            temp.append(arr[i][j])
            diagonal.append(sum(temp))

    for i in range(n):
        for j in range(n):
            temp = []
            for a in range(1,m):
                if i - a >= 0:
                    temp.append(arr[i - a][j])
                if i + a < n:
                    temp.append(arr[i + a][j])
                if j - a >= 0:
                    temp.append(arr[i][j - a])
                if j + a < n:
                    temp.append(arr[i][j + a])
            temp.append(arr[i][j])
            line.append(sum(temp))
    print(f"#{tc} {max(max(line), max(diagonal))}")