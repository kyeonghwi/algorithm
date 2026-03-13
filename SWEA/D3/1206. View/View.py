T = 10
for tc in range(1, T+1):
    n= int(input())
    arr=list(map(int,input().split()))
    result = 0
    for i in range(2,n-2):
        out = max(arr[i - 2], arr[i - 1], arr[i + 1], arr[i + 2])
        if arr[i]>out:
            out = arr[i] -out
            result+=out
    print(f"#{tc} {result}")