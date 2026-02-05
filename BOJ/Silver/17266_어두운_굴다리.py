import sys

input = sys.stdin.readline
n= int(input())
m= int(input())
arr =list(map(int,input().split()))

zero = arr[0]
last = n - arr[-1]
length = max(zero, last)
for i in range(1,m):
    temp = (arr[i] - arr[i-1] +1)//2
    length = max(temp, length)
print(length)