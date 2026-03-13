import sys

input = sys.stdin.readline
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
k = int(input())
day = [0] * 32
for elem in arr:
    for x in range(elem[0],elem[1]):
       day[x] +=1
if max(day) > k:
    print(0)
else:
    print(1)