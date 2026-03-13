import sys

input = sys.stdin.readline
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
_ = int(input())
k1 = arr1.pop(0)
k2 = arr2.pop(0)

for i in range(k1):
