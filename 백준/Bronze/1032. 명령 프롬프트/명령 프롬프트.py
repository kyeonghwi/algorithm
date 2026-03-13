import sys

input = sys.stdin.readline
n = int(input())
ans =[]
s = input().strip()
for elem in s:
    ans.append(elem)
for _ in range(n-1):
    s = input().strip()
    for i in range(len(ans)):
        if ans[i] != s[i]:
            ans[i] = "?"
print(*ans,sep="")