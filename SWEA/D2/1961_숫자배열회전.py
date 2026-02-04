T = int(input())
for tc in range(1, T + 1):
    n= int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    arr90=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            arr90[i][j] = arr[n-1-j][i]

    arr180=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            arr180[i][j] = arr90[n - 1 - j][i]

    arr270=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            arr270[i][j] = arr180[n - 1 - j][i]

    print(f"#{tc}")

    for i in range(n):
        row90="".join(map(str,arr90[i]))
        row180="".join(map(str,arr180[i]))
        row270="".join(map(str,arr270[i]))
        print(f"{row90} {row180} {row270}")