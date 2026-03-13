import sys

input = sys.stdin.readline

n = int(input())
for T in range(n):
    arr = list(map(int,input().split()))
    arr.pop(0)
    a= max(arr)
    b=min(arr)
    c = 0
    arr.sort(reverse=True)
    for i in range(1,len(arr)):
        temp = abs(arr[i] - arr[i-1])
        c = max(c,temp)
    print("MAX ",a,end=" ")
    print("MIN ",b,end=" ")
    print(f"Class {T+1}")
    print(f"Max {a} Min {b} Largest gap {c}")