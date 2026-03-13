n, m= map(int,input().split())
sx,sy=map(int,input().split())
ex,ey=map(int,input().split())

if((sx-ex)%2 == (sy-ey)%2):
    print("yes")
else:
    print("no")