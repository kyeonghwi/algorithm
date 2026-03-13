import sys

input = sys.stdin.readline
n, m = map(int,input().split())
arr = [input().strip() for _ in range(n)]
num = {name: idx+1 for idx, name in enumerate(arr)}
for _ in range(m):
    pro = input().strip()
    if pro.isdigit():
        print(arr[int(pro)-1])
    else:
        print(num[pro])