import sys

input = lambda: sys.stdin.readline().rstrip()

cnt =0

n = int(input())
while (n>0):
    cnt += n//5
    n= n//5
print(cnt)