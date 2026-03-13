T = int(input())
for tc in range(1, T + 1):
    n, k = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]

    cnt=0
    for i in range(n):
        word= 0
        for j in range(n):
            if arr[i][j]==1:
                word+=1
            else:
                if word == k:
                    cnt += 1
                word=0
        if word ==k:
            cnt += 1
    for j in range(n):
        word= 0
        for i in range(n):
            if arr[i][j]==1:
                word+=1
            else:
                if word == k:
                    cnt += 1
                word=0
        if word == k:
            cnt += 1
    print(f"#{tc} {cnt}")