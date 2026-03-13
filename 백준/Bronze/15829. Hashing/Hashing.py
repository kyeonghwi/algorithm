import sys

input = sys.stdin.readline
n = int(input())
arr = input().strip()
encrypt = 0
m=1234567891
for i,elem in enumerate(arr):
    temp = ord(elem)- ord('a') + 1
    encrypt +=temp*(31**i)
print(encrypt % m)