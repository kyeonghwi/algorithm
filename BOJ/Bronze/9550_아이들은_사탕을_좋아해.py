t= int(input())
for _ in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    child=0
    for elem in arr:
        child += elem//k
    print(child)