h,m = map(int, input().split())
c= int(input())
h += c//60
m+= c%60
if m>59:
    m-=60
    h+=1
if h>23 :
    h-=24
    
print(h, m)