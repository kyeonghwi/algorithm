import sys

input = sys.stdin.readline
n, m = map(int,input().split())
arr= list(map(int,input().split()))

arr.sort()
s=[]
visited=[False] * n
def dfs():
    if len(s) == m:
        print(" ".join(map(str, s)))
        return

    last_used = 0
    for i in range(n):
        if not visited[i] and last_used!= arr[i]:
            s.append(str(arr[i]))
            visited[i] = True
            last_used = arr[i]
            dfs()
            s.pop()
            visited[i] = False
dfs()