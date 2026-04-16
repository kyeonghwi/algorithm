n,m = map(int, input().split())
a=[0]*(n+1)
for _ in range(m):
    x,y,z=map(int,input().split())
    for i in range(x,y+1):
        a[i] = z
for k in range(1,n+1):
    print(a[k], end=" ")
