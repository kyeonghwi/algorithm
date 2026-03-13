t = int(input())
sw=0
im=0
ai=0
nothing=0
for i in range(t):
    g,c,n = map(int,input().split())
    if g==1:
        nothing+=1
    elif c==1 or c==2:
        sw+=1
    elif c==3:
        im+=1
    elif c==4:
        ai+=1
print(sw)
print(im)
print(ai)
print(nothing)