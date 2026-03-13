n = int(input())
cnt=0
i=1
while n > cnt:
    cnt += i
    i+=1
i-=1
cnt-=i
pos = n -cnt
if i %2==0:
    a, b = pos , i -pos +1
else:
    b, a = pos, i - pos + 1

print(f"{a}/{b}")