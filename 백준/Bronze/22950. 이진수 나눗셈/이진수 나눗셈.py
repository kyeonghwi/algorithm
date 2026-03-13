import sys
input = sys.stdin.readline

N = int(input())
M = input().strip()
K = int(input())

if '1' not in M:
    print("YES")
    exit(0)

if K == 0:
    print("YES")
    exit(0)

if M[-K:] == '0' * K:
    print("YES")
else:
    print("NO")