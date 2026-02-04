T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    S = []
    for i in range(N+M):
        if i < N:
            S.append(A[i])
        if i < M:
            S.append(B[i])
    print(f'#{tc} {" ".join(map(str, S))}')
