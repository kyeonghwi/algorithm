import sys
input = sys.stdin.readline
n, k = map(int,input().split())
arr=[]
result = []
for i in range(1,n+1):
    arr.append(i)
current = 0
while len(arr) > 0:
    current += k - 1
    if current >= len(arr):
        current %= len(arr)
    result.append(arr.pop(current))
print(f"<{', '.join(map(str,result))}>")