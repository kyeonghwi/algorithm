import sys

input = sys.stdin.readline
n, m = map(int,input().split())
s = []
visited=[False]*(n+1)
def dfs():
    if len(s)==m:
        print(' '.join(s))
        return
    for i in range(1,n+1):
        if not s or (s and (int(s[-1]) <= i)):
            s.append(str(i))
            dfs()
            s.pop()
dfs()
