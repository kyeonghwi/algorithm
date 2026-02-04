import sys

input = sys.stdin.readline
s,n,m = map(int,input().split())

arr =[]
length=s
for i in range(n+m):
    a = int(input())
    if a==1:
        if len(arr)==length:
            length +=length
        arr.append(1)
    else:
        arr.pop()
print(length)