n,m = map(int,input().split())
a = [i for i in range(1,n+1)]
for _ in range(m):
    i,j = map(int,input().split())
    temp = a[i-1]
    a[i-1]=a[j-1]
    a[j-1]=temp
for i in range(n):
    print(a[i],end=" ")
    
    