import sys

input = sys.stdin.readline
n, m = map(int,input().split())
arr= list(map(int,input().split()))

arr = sorted(set(arr))
s=[]
def dfs():
    if len(s)==m:
        print(*s)
        return
    for i in range(len(arr)):
        if not s or (s and arr[i] >= s[-1]):
            s.append(arr[i])
            dfs()
            s.pop()
dfs()