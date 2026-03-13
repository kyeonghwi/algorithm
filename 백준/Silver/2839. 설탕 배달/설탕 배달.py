import sys

input = sys.stdin.readline
n = int(input())
possible = False
for five in range(n//5,-1,-1):
    if (n - five*5) %3==0:
        three = (n - five*5)//3
        possible=True
        break
if possible:
    print(five+three)
else:
    print(-1)