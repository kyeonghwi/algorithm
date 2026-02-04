import sys

input = sys.stdin.readline
k = int(input())
num = []
for _ in range(k):
    n = int(input().strip())
    if n == 0:
        num.pop()
    else:
        num.append(n)
print(sum(num))