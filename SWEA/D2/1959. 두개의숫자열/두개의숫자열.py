T = int(input())
for tc in range(1, T + 1):
    n, m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    if n > m:
        n,m = m, n
        a,b = b,a
    maxv =0
    for i in range(m - n +1):
        result = 0
        for j in range(n):
            temp = a[j]*b[j+i]
            result += temp
        maxv = max(result, maxv)
    print(f"#{tc} {maxv}")