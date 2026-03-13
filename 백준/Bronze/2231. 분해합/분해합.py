import sys

input = sys.stdin.readline
n = int(input())
for i in range(1, n+1):
    total = sum(map(int,str(i))) + i
    if total == n:
        print(i)
        break
    if i==n:
        print(0)