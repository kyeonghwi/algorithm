import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
t, p =map(int,input().split())
total=0
for elem in arr:
    if elem%t==0:
        total += elem//t
    else:
        total +=elem//t + 1
print(total)
print(n//p, n%p)