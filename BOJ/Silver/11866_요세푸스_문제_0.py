import sys

input = sys.stdin.readline
n, m = map(int,input().split())
arr= []
for i in range(1,n+1):
    arr.append(i)
print("<",end="")
jump=0
for i in range(n):
    jump = (jump + (m-1))%len(arr)
    print(arr.pop(jump),end="")
    if len(arr) !=0:
        print(end=", ")
print(">")