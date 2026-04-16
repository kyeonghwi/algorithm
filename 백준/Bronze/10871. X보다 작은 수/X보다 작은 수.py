n,x = map(int, input().split())
k = list(map(int,input().split()))
for i in range(n):
    if k[i] < x:
        print(k[i], end=" ")