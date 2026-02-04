import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
arr.append(arr[0])
total =0
for i in range(n):
    total += arr[i][0]*arr[i+1][1] - arr[i+1][0]*arr[i][1]
print(f"{abs(total)/2}")