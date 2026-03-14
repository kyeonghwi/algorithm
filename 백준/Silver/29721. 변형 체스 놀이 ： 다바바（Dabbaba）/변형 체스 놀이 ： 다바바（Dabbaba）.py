import sys

input = sys.stdin.readline

N, K = map(int, input().split())

move_count = dict()
piece_coordinate = dict()

for _ in range(K):
    X, Y = map(int, input().split())

    piece_coordinate[(X, Y)] = True

dx = [0, 2, 0, -2]
dy = [2, 0, -2, 0]

for X, Y in piece_coordinate.keys():
    
    for i in range(4):
        DX, DY = X + dx[i], Y + dy[i]

        if not ((1 <= DX <= N) and (1 <= DY <= N)):
            continue

        if (DX, DY) in piece_coordinate:
            continue

        if (DX, DY) in move_count:
            continue

        move_count[(DX, DY)] = 1

print(len(move_count))