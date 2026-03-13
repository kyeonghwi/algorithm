import sys

input = sys.stdin.readline
n = int(input())
print('@'*(n+2))
for _ in range(n):
    print('@',end=" "*n)
    print('@')
print('@' * (n + 2))
