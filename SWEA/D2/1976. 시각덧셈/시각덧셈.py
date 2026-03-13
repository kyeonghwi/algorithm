T = int(input())
for tc in range(1,T+1):
    h1,m1,h2,m2 = map(int,input().split())
    h,m= 0,0
    if (m1+m2) >59:
        m=m1+m2-60
        h=1
    else:
        m = m1 + m2
    if (h1+h2) >11:
        h += h1+h2-12
    else:
        h += h1 + h2
    print(f"#{tc} {h} {m}")