import sys

input = sys.stdin.readline
n = int(input())
x = 0
for i in range(n):
    a = int(input())
    pot = a %10
    a= a//10
    x +=a**pot
print(x)
