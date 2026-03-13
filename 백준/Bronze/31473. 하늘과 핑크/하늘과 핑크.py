import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
a= sum(list(map(int,input().split())))
b= sum(list(map(int,input().split())))

print(a,b)