for k in range(1,11):
    n = int(input())
    arr = [list(input().strip()) for _ in range(8)]
    cnt =0
    for j in range(8):
        for i in range(8 - n + 1):
            if all(arr[i+a][j] == arr[i+n-1-a][j] for a in range(n//2)):
                cnt += 1

    # 가로 회문 검사 (행 고정)
    for i in range(8):
        for j in range(8 - n + 1):
            if all(arr[i][j+a] == arr[i][j+n-1-a] for a in range(n//2)):
                cnt += 1

    print(f"#{k} {cnt}")				