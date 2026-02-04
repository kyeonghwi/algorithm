import sys

input = sys.stdin.readline
n = int(input())
arr=list(map(int,input().split()))
highest=0
end=0
start=arr[0]
for n in range(len(arr)-1):
    if arr[n] >= arr[n+1]:
        start = arr[n+1]
        end=0
    elif arr[n] < arr[n+1]:
        end=arr[n+1]
    highest = max(highest, end - start)
print(highest)