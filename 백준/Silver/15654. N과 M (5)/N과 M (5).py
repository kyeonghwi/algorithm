import sys
from pickle import FALSE

input = sys.stdin.readline
n, m = map(int,input().split())
arr = list(map(int,input().split()))
s=[]
arr.sort()
visited = [False] * (n+1)
def dfs():
    if len(s)==m:
        print(" ".join(s))
        return
    for i, elem in enumerate(arr):
        if not visited[i]:
            s.append(str(elem))
            visited[i] = True
            dfs()
            s.pop()
            visited[i] = False
dfs()