import sys

input = sys.stdin.readline
x, y = map(int,input().split())
a, b = 100 - x, 100-y
c, d = 100 - (a+b), a*b
q, r = d//100, d%100

print(a,b,c,d,q,r)
if d<10:
    print(c, d)
else:
    print(c+q, r)