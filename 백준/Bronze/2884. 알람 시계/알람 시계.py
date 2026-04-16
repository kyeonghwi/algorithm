a,b = map(int, input().split())
if b<45:
    if a==0:
        a=a+23
        b= b+15
        print(a, b)
    else :
        a= a-1
        b= b+15
        print(a, b)
else :
    b=b-45
    print(a, b)