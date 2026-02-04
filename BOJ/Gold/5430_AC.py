import sys
from collections import deque

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    p = input().strip()
    n = int(input())
    arr = deque(input().strip()[1:-1].split(','))
    if n == 0:
        arr = deque()
    error=False
    cnt=0
    for com in p:
        if com =="R":
            cnt+=1
        elif not arr:
            error = True
            break
        elif com =="D":
            if cnt %2==0:
                arr.popleft()
            else:
                arr.pop()

    if not error:
        if cnt %2==1:
            arr.reverse()
        print(f"[{','.join(map(str,arr))}]")
    else:
        print('error')