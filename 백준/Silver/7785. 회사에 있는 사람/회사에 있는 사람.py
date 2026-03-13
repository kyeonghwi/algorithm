import sys

input = sys.stdin.readline
n = int(input())
com = set()
for _ in range(n):
    man, state = input().split()
    if state == "enter":
        com.add(man)
    else:
        com.discard(man)
com = sorted(com, reverse=True)
for elem in com:
    print(elem)