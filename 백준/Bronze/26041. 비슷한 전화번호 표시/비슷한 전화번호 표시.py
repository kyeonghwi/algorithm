import sys

input = lambda: sys.stdin.readline().rstrip()
arr=list(map(str,input().split()))
n = input().strip()
cnt=0
for elem in arr:
    if elem.startswith(n) and elem !=n:
        cnt+=1
print(cnt)