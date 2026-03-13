import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    h,w,n = map(int, input().split())
    room = n//h +1
    if n%h==0:
        room-=1
        floor = h*100
    else:
        floor = n%h*100
    num = room+floor
    print(num)