import sys

input = sys.stdin.readline
n, m = map(int,input().split())
for i in range(min(n,m), 0, -1):
    if n%i==0 and m%i==0:
        gcd = i
        print(gcd)
        print(n*m//gcd)
        break