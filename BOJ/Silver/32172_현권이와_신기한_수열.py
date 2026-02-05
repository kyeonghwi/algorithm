import sys

input = sys.stdin.readline
n = int(input())

visited = set()
A = 0
visited.add(A)

for i in range(1, n+1):
    nextA = A - i
    if nextA < 0 or nextA in visited:
        nextA = A + i
    visited.add(nextA)
    A = nextA

print(A)