import sys

input = lambda: sys.stdin.readline().rstrip()

while True:
    n,m = map(int,input().split())
    if n==0 and m==0:
        break
    call = [list(map(int,input().split())) for _ in range(n)]
    for _ in range(m):
        cnt=0
        cop_start, cop_duration = list(map(int, input().split()))
        for s,d,start,dura in call:
            if (start < cop_start+ cop_duration) and (start+dura > cop_start):
                cnt+=1
        print(cnt)