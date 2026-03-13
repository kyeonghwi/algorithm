import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
for _ in range(n):
    print("@"*n*5)
for _ in range(n*3):
    print("@"*n,end="")
    print(" "*3*n,end="")
    print("@"*n)
for _ in range(n):
    print("@"*n*5)