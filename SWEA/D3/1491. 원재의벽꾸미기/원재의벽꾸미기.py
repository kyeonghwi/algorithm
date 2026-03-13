T = int(input())
for tc in range(1, T+1):
    n,a,b = map(int,input().split())

    result = 9999999
    for i in range(1,int(n**0.5)+2):
        for j in range(1,n//i+1):
            if i* j <= n:
                temp = a*abs(i -j) + b*abs(n-i*j)
                result = min(temp,result)
    print(f"#{tc} {result}")