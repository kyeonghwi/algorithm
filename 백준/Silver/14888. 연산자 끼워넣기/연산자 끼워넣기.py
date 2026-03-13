import sys

input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
op = list(map(int,input().split()))

maximum = -1e9 -1
minimum = 1e9 + 1

def dfs(cnt, total, plus, minus, multi, divide):
    global maximum, minimum
    if cnt ==n:
        maximum = max(maximum, total)
        minimum = min(minimum, total)
        return
    if plus:
        dfs(cnt+1, total + a[cnt], plus-1, minus, multi, divide)
    if minus:
        dfs(cnt+1, total - a[cnt], plus, minus-1, multi, divide)
    if multi:
        dfs(cnt+1, total * a[cnt], plus, minus, multi-1, divide)
    if divide:
        dfs(cnt+1, int(total / a[cnt]), plus, minus, multi, divide-1)
dfs(1,a[0],op[0],op[1],op[2],op[3])
print(maximum)
print(minimum)