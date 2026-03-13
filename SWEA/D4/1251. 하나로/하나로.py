T = int(input())
for tc in range(1, T+1):
     N = int(input()) # 섬 개수 N
     X = list(map(int, input().split())) #섬 좌표 X
     Y = list(map(int, input().split())) #섬 좌표 Y
     E = float(input()) # 세금 E

     adj_m = [[0]*N for _ in range(N)]

     for i in range(N):
         for j in range(N):
             if i != j:
                 LL = (X[i] - X[j])**2 + (Y[i] - Y[j])**2
                 cost = LL * E
                 adj_m[i][j] = cost
                 adj_m[j][i] = cost
         for row in adj_m:
             print(row)


