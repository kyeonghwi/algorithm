import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
length = sum(arr)
arr.sort(reverse=True)
cost=0
for elem in arr:
    length -=elem
    cost += length *elem
print(cost)