import sys

input = lambda: sys.stdin.readline().rstrip()
n,m,a,b = list(map(int,input().split()))
if 3*n <=m:
    print('0')
else:
    print((3*n - m)*a+b)