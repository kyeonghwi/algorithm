import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    arr = list(map(int,input().split()))
    arr.sort()
    if (arr[3]-arr[1] >= 4):
        print("KIN")
    else:
        print(sum(arr[1:4]))