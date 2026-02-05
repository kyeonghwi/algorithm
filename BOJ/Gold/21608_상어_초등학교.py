import sys

input = sys.stdin.readline

def in_range(x,y):
    return 0<=x<n and 0<=y<n

n = int(input())
data = [[0] * n for _ in range(n)]
students = [list(map(int, input().split())) for _ in range(n**2)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for stu in students:
    available =[]
    for i in range(n):
        for j in range(n):
             if data[i][j] == 0:
                prefer, empty = 0, 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if in_range(nx,ny):
                        if data[nx][ny] in stu[1:]:
                            prefer += 1
                        if data[nx][ny] == 0:
                            empty += 1
                available.append((i, j, prefer, empty))
    available.sort(key= lambda x: (-x[2], -x[3], x[0], x[1]))
    data[available[0][0]][available[0][1]] = stu[0]
total =0
students.sort()
for i in range(n):
    for j in range(n):
        cnt=0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if in_range(nx,ny):
                if data[nx][ny] in students[data[i][j] - 1]:
                    cnt += 1
        if cnt==0:
            continue
        elif cnt==1:
            total+=1
        elif cnt==2:
            total+=10
        elif cnt==3:
            total+=100
        elif cnt==4:
            total+=1000
print(total)