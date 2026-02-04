import sys

input = sys.stdin.readline
n, m = map(int,input().split())
prime=[True]*(m+1)
prime[0], prime[1] = False, False
for i in range(2,m+1):
    if prime[i]:
        for j in range(i*2,m+1,i):
            prime[j]=False
for k in range(n,m+1):
    if prime[k]:
        print(k)