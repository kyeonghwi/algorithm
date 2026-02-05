import sys

input = sys.stdin.readline
h, w = map(int,input().split())

for _ in range(h):
    arr = list(input())
    cnt=0
    for i in range(w):
        if arr[i]=='c':
            print('0', end=" ")
            cnt=1
        elif arr[i]=="." and cnt!=0:
            print(cnt, end=" ")
            cnt+=1
        else:
            print('-1',end=" ")
    print()
    