import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
arr.sort()
result = []
for elem in arr:
    if elem not in result:
        result.append(elem)
print(*result)