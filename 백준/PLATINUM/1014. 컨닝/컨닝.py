import sys
input = sys.stdin.readline

# 이분 매칭
def bip_match(x, y):
	# 컨닝가능한 6방향 체크
    for i in range(len(d_x)):
        dx = x+d_x[i]
        dy = y+d_y[i]
        if not (0 <= dx < n and 0 <= dy < m):
            continue
        # 이미 완료된 정점은 시도하지 않음
        if graph[dx][dy] == 'x' or done[dx][dy]:
            continue
        done[dx][dy] = 1
        # 점유한 정점이 없거나 양보가 가능한 경우
        if not link[dx][dy] or bip_match(*link[dx][dy]):
            link[dx][dy] = [x, y]
            return 1
    return 0
    
t = int(input())
d_x = [-1, 0, 1, -1, 0, 1]
d_y = [-1, -1, -1, 1, 1, 1]
for _ in range(t):
    n, m = map(int, input().rstrip().split())
    graph = [input() for _ in range(n)]
    # 
    link = [[0]*m for _ in range(n)]
    # 앉을 수 있는 자리의 최대값
    seat_num = n*m
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'x':
                seat_num -= 1
                continue
            if not j%2:
                continue
            done = [[0]*m for _ in range(n)]
            # 매칭이 되었다면 앉을 수 없는 자리임
            seat_num -= bip_match(i, j)
    print(seat_num)
