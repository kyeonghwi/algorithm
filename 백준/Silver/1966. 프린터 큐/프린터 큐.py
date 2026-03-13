import sys

input = sys.stdin.readline
t = int(input())
for tc in range(t):
    n, m = map(int,input().split())
    arr = list(map(int,input().split()))
    wanted = [0] * n
    wanted[m] +=1
    cnt=0
    while 1 in wanted:
        if arr[0] != max(arr):
            arr.append(arr.pop(0))
            wanted.append(wanted.pop(0))
        else:
            cnt+=1
            arr.pop(0)
            v = wanted.pop(0)
            if v == 1:
                print(cnt)
                break
