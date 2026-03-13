import sys

input = sys.stdin.readline
n, k = map(int,input().split())
up =1
for i in range(n,n-k,-1):
    up *= i
for i in range(1,k+1):
    up //=i
print(up)