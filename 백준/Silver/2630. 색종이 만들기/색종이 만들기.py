import sys

input = sys.stdin.readline
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
w_cnt, b_cnt = 0, 0
def divide(x,y,n):
    global w_cnt
    global b_cnt
    initial = arr[x][y]
    mixed =False
    for i in range(x,x+n):
        for j in range(y,y+n):
            if arr[i][j] != initial:
                mixed = True
                break
        if mixed:
            break
    if mixed:
        divide(x,y,n//2)
        divide(x+n//2,y,n//2)
        divide(x,y+n//2,n//2)
        divide(x+n//2,y+n//2,n//2)

    else:
        if initial ==0:
            w_cnt+=1
        else:
            b_cnt+=1
divide(0,0,n)
print(w_cnt)
print(b_cnt)