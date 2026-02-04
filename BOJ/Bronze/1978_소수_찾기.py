import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
cnt=0
for elem in arr:
    if elem !=1:
        if all(elem%i!=0 for i in range(2,elem)):
            cnt+=1
print(cnt)