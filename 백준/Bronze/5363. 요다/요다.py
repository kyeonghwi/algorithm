import sys

input = sys.stdin.readline
n = int(input())
for i in range(n):
    arr = list(input().split())
    arr = arr[2:] + arr[0:2]
    for elem in arr:
        print(elem, end=" ")
    print()
