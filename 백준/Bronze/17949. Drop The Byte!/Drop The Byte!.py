import sys

input = sys.stdin.readline
arr = input().strip()
n= int(input())
types = list(input().split())

result = []
for type in types:
    if type=="int":
        temp = arr[:8]
        arr = arr[8:]
    elif type == "char":
        temp = arr[:2]
        arr = arr[2:]
    else:
        temp = arr[:16]
        arr =arr[16:]
    decimal = int(temp, 16)
    result.append(decimal)
print(*result)