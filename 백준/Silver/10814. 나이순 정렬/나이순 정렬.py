import sys

input = sys.stdin.readline
n = int(input())
arr = [list(input().split()) for _ in range(n)]
arr.sort(key = lambda x:int(x[0]))
for elem in arr:
    for k in elem:
        print(k, end=" ")
    print()