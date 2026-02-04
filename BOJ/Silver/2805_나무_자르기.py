import sys

input = sys.stdin.readline
n, m = map(int,input().split())
arr = list(map(int,input().split()))
start = 1
end= max(arr)
result =0
while start <= end:
    mid = (start + end)//2
    cut = 0
    for elem in arr:
        if elem > mid:
            cut += elem - mid
    if cut >= m:
        result = mid
        start = mid +1
    else:
        end = mid-1
print(result)