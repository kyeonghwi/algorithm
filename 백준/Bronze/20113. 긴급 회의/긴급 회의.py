import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
arr =list(map(int,input().split()))

skip=0
vote=[0]*(n+1)
for elem in arr:
    if elem ==0:
        skip+=1
    else:
        vote[elem]+=1
cnt=0
temp=max(vote)
for elem in vote:
    if elem == temp:
        cnt+=1
        ans =elem
if cnt > 1 or (temp < skip):
    print("skipped")
else:
    print(vote.index(temp))