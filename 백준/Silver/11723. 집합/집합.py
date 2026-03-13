import sys

input = sys.stdin.readline
n = int(input())
s =set()
for _ in range(n):
    command = input().split()
    com = command[0]
    if com=="add":
        s.add(int(command[1]))
    elif com=="remove":
        s.discard(int(command[1]))
    elif com=="check":
        if int(command[1]) in s:
            print(1)
        else:
            print(0)
    elif com == "toggle":
        if int(command[1]) in s:
            s.discard(int(command[1]))
        else:
            s.add(int(command[1]))
    elif com=="all":
        s = set(range(1, 21))
    elif com=="empty":
        s =set()

