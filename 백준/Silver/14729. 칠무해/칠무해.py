import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
arr=[]
for _ in range(n):
    temp = float(input())
    arr.append(temp)

arr.sort()
for score in arr[:7]:
    print(f"{score:.3f}")