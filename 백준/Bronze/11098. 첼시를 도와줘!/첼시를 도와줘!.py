import sys

input = lambda: sys.stdin.readline().rstrip()
t = int(input())
for _ in range(t):
    n = int(input())
    p =-1
    for _ in range(n):
        price, name = input().split()
        if int(price) >p:
            player = name
            p = int(price)
    print(player)