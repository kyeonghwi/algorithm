import sys

input = sys.stdin.readline
n = int(input())
t = list(map(int,input().split()))
study = sum(t) + 8*(n-1)
print(study//24,study%24)