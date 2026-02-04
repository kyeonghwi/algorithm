import sys

input = lambda: sys.stdin.readline().rstrip()
n, s = map(int,input().split())
arr=list(map(int,input().split()))

start, end =0,0
current =0
min_len=float('inf')

while True:
    if current >= s:
        min_len = min(min_len,end -start)
        current -= arr[start]
        start+=1
    elif end==n:
        break
    else:
        current +=arr[end]
        end+=1

if min_len==float('inf'):
    print(0)
else:
    print(min_len)