import sys
input = sys.stdin.readline
n = int(input())
arr = [(input()) for _ in range(n)]
arr.sort(key = lambda x:[len(x), x])
result = []
for elem in arr:
    if elem not in result:
        result.append(elem)
        print(elem)