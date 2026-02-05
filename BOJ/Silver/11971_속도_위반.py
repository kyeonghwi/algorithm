n,m=map(int,input().split())
limit=[0]*101
speed=[0]*101
temp=1
for _ in range(n):
    dis, vel = map(int,input().split())
    limit[temp:temp + dis] = [vel]*dis
    temp +=dis

temp2 = 1
for _ in range(m):
    dis, vel = map(int, input().split())
    speed[temp2 : temp2 + dis] = [vel] * dis
    temp2 += dis

overflow=0
for i in range(1,101):
    overflow = max(overflow,speed[i]-limit[i])
print(overflow)