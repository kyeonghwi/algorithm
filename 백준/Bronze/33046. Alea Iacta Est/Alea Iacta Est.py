sum=-1
for _ in range(2):
    a,b=map(int,input().split())
    sum += a+b
if(sum%4==0):
    print(4)
else:
    print(sum%4)