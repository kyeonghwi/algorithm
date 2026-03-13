import sys

input = lambda: sys.stdin.readline().rstrip()

n,a,b,c = map(int,input().split())

def calc(c):
    if c==1:
        return 1
    else:
        return c*calc(c-1)

print(int(calc(n)/(calc(a)*calc(b)*calc(c))))