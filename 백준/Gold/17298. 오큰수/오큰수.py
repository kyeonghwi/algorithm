import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
ans = [-1] * n
stack =[0]

for i in range(1,n):
    while stack and a[stack[-1]]<a[i]: 
        ans[stack[-1]] = a[i]
        stack.pop()
    stack.append(i)
print(*ans)