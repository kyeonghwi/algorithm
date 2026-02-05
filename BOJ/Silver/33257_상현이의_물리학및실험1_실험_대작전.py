import sys

input = sys.stdin.readline
n, e = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

cnt=1
for i in range(1,n):
    if (arr[i] - arr[i-1]) >= e:
        cnt+=1
print(cnt)