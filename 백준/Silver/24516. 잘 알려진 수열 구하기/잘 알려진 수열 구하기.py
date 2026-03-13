import sys

input = sys.stdin.readline
n= int(input())

start = 1
result = []
for _ in range(n):
    result.append(start)
    start +=2
    
print(*result)