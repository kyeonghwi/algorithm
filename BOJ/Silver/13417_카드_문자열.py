from collections import deque
import sys

input = sys.stdin.readline

T = int(input())
for t in range(T):
    n = int(input())
    arr = input().split()
    q =deque()
    q.append(arr[0])
    st = arr[0]
    for i in range(1,n):
        if st>=arr[i]:
            q.appendleft(arr[i])
            st = arr[i]
        else:
            q.append(arr[i])
    print(''.join(q))