import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
arr = list(map(int,input().split()))

bit=[0]*32

def calc(x):
    temp = x
    k = 0
    while temp >0:
        bit[k] += temp%2
        temp = temp//2
        k+=1

for elem in arr:
    calc(elem)
    
print(max(bit))