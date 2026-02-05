t = int(input())

for _ in range(t):
    n,c = map(int,input().split())
    if n%c >0:
        print(n//c +1)
    else:
        print(n//c)