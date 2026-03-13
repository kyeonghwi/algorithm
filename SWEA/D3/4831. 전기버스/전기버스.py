T = int(input())
for tc in range(1, T + 1):
    k, n, m = map(int,input().split())
    arr = list(map(int,input().split()))

    cnt = bus = 0
    while bus + k < n:
        for step in range(k,0,-1):
            if (bus + step) in arr:
                bus += step
                cnt+=1
                break
        else:
            cnt=0
            break
    print(f"#{tc} {cnt}")