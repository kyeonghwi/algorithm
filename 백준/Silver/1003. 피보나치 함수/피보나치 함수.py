import sys

input = sys.stdin.readline
T = int(input())
for tc in range(1,T+1):
    n = int(input())
    a,b = 1,0
    for i in range(n):
        a,b = b, a+b
    print(a,b)