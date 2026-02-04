import sys

input = sys.stdin.readline

MAX_NUM = 123456 *2
primes = [True] * (MAX_NUM+1)
primes[0] = primes[1] = False

for i in range(2,int(MAX_NUM**0.5) + 1):
    if primes[i]:
        for j in range(i*2, MAX_NUM+1,i):
            primes[j] = False

while True:
    n = int(input().strip())
    if n==0:
        break
    cnt=sum(primes[n+1:2*n+1])
    print(cnt)