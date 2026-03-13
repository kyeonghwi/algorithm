import sys
from collections import deque

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    a, b = map(int,input().split())
    queue = deque()
    queue.append(a)

    visited = [] * 10000
    visited[a] = (-1,"")

    while queue:
        n= queue.popleft()
        if n ==b:
            break
        num = n*2 % 10000
        if not visited[num]:
            visited[num] = (n,"D")
            queue.append(num)

        num = n-1 if n != 0 else 9999
        if not visited[num]:
            visited[num] = (n,"S")
            queue.append(num)

        num = (n % 1000) * 10 + (n // 1000)
        if not visited[num]:
            visited[num] = (n,"L")
            queue.append(num)

        num = (n % 10) * 1000 + (n // 10)
        if not visited[num]:
            visited[num] = (n,"R")
            queue.append(num)
    answer = ""
    curr = b
    while curr!=a:
        parent, cmd = visited[curr]
        answer +=cmd
        curr = parent
    print(answer[::-1])