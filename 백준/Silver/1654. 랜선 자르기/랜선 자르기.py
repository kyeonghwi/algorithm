import sys

input = sys.stdin.readline
k, n = map(int,input().split())
arr = [int(input().strip()) for _ in range(k)]

start = 1
end= max(arr)
while start <= end:
    length = (start+end)//2
    temp =0
    for elem in arr:
        temp += elem//length
    if temp>= n:
        start =length + 1
    else:
        end =length - 1
print(end)
