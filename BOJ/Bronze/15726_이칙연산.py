import sys

input = sys.stdin.readline
a,b,c = map(int,input().split())
max_v = a*b/c
min_v = a/b*c
print(int(max(max_v,min_v)))