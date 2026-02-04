import sys

input = sys.stdin.readline
n, k = map(int,input().split())
arr = [int(input()) for _ in range(n)]
arr.sort(reverse= True)
cnt = 0
while k!=0:
    for i in range(n):
        if k//arr[i] >0:
            cnt +=k//arr[i]
            k = k-k//arr[i]*arr[i]
print(cnt)