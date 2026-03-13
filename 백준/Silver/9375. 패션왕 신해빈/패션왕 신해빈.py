import sys
from collections import defaultdict

input = sys.stdin.readline
T = int(input().strip())
for tc in range(T):
    n = int(input().strip())
    arr = defaultdict(list)
    for _ in range(n):
        name, cloth = input().split()
        arr[cloth].append(name)
    cnt=1
    for elem in arr:
        cnt *= (len(arr[elem])+1)
    print(cnt-1)