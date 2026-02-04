T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())

    xyc = [list(map(int, input().split())) for _ in range(M)]

    adj_m = [[0]*(N+1) for _ in range(N+1)]

    for x, y, c in xyc:
        adj_m[x][y] = c # 인접이면 비용 c 아니면 0
    '''
    for x, y, c in xyc:
        adj_list[x].append((y,c))
    '''
    for row in adj_m:
        print(row)