import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
arr_sorted = sorted(list(set(arr)))
coo ={}
for i in range(len(arr_sorted)):
    coo[arr_sorted[i]]=i
for i in arr:
    print(coo[i],end=" ")