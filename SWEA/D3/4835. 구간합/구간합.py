T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = list(map(int,input().split()))

    min_v = 1000000
    max_v = 0

    for i in range(N-M+1):
        s = 0
        for j in range(M):
            s += arr[i+j]
        #for j in range(i, i+M):
            #s += arr[j]
        if min_v > s:
            min_v = s
        if max_v < s:
            max_v = s

    print(f'#{tc} {max_v - min_v}')