T = int(input())
for tc in range(1, T + 1):
    h,w = map(int,input().split())
    arr = [list(input().strip()) for _ in range(h)]
    n= int(input())
    command = list(input().strip())

    for i in range(h):
        for j in range(w):
            if arr[i][j] in ("<", ">", "^", "v"):
                x ,y = i, j
                break
    for elem in command:
        if elem =="S":
            dx ,dy = 0,0
            if arr[x][y] == '<':
                dy = -1
            elif arr[x][y] == '>':
                dy = 1
            elif arr[x][y] == '^':
                dx = -1
            elif arr[x][y] == 'v':
                dx = 1

            nx, ny =x+dx, y+dy
            while 0<= nx<h and 0<=ny<w:
                if arr[nx][ny] == '#': break
                if arr[nx][ny] == '*':
                    arr[nx][ny] = '.'
                    break
                nx += dx
                ny += dy
        elif elem == "U":
            arr[x][y] = "^"
            new_x, new_y = x - 1, y
            if 0 <= new_x < h and arr[new_x][new_y] == ".":
                arr[x][y] = "."
                x = new_x
                arr[x][y] = "^"

        elif elem == "D":
            arr[x][y] = "v"
            new_x, new_y = x + 1, y
            if 0 <= new_x < h and arr[new_x][new_y] == ".":
                arr[x][y] = "."
                x = new_x
                arr[x][y] = "v"

        elif elem == "L":
            arr[x][y] = "<"
            new_x, new_y = x, y - 1
            if 0 <= new_y < w and arr[new_x][new_y] == ".":
                arr[x][y] = "."
                y = new_y
                arr[x][y] = "<"

        elif elem == "R":
            arr[x][y] = ">"
            new_x, new_y = x, y + 1
            if 0 <= new_y < w and arr[new_x][new_y] == ".":
                arr[x][y] = "."
                y = new_y
                arr[x][y] = ">"

    print(f"#{tc}", end=" ")
    for i in range(h):
        print("".join(map(str,arr[i])))