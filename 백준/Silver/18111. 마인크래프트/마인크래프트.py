import sys

input = sys.stdin.readline
n, m, b = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
min_h = min(map(min, arr))
max_h = max(map(max, arr))
result_time = float('inf')
result_height = 0
for h in range(min_h, max_h+1):
    time = 0
    block = b
    for i in range(n):
        for j in range(m):
            diff = arr[i][j] - h
            if diff>0:
                time += diff*2
                block +=diff
            elif diff<0:
                time +=-diff
                block -= -diff
    if block>=0:
        if time < result_time or (time ==result_time and h > result_height):
            result_time = time
            result_height = h
print(result_time, result_height)