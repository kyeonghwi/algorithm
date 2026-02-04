import sys

input = sys.stdin.readline
n, m = map(int,input().split())
hear={input().strip() for _ in range(n)}
nothing=[]
for _ in range(m):
    temp = input().strip()
    if temp in hear:
        nothing.append(temp)
print(len(nothing))
nothing.sort()
for i in nothing:
    print(i)