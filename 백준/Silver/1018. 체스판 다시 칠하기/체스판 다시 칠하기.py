import sys

input = sys.stdin.readline
n, m = map(int,input().split())
arr = [list(input().strip()) for _ in range(n)]
cnt=32
for row in range(n-7):
    for col in range(m-7):
        count_w = 0
        count_b= 0

        for i in range(row,row+8):
            for j in range(col, col+8):
                if (i+j)%2==0:
                    if arr[i][j] !='W':
                        count_w+=1
                    if arr[i][j] != 'B':
                        count_b += 1
                else:
                    if arr[i][j] !='B':
                        count_w+=1
                    if arr[i][j] != 'W':
                        count_b += 1
        current_min = min(count_w, count_b)
        cnt = min(current_min, cnt)
print(cnt)