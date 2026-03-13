T = int(input())
for tc in range(1, T + 1):
    p,q = map(int,input().split())

    def xy_num(x,y):
        d = x+y-1
        return (d-1) * d // 2 + x

    def num_xy(num):
        temp = num
        cnt =0
        xy=[0,0]

        while True:
            cnt +=1
            temp -= cnt
            if temp <=0:
                break
        temp = temp+ cnt
        xy[0] = temp
        xy[1] = cnt +1 - temp

        return xy
    def calc(p, q):
        p_xy = num_xy(p)
        q_xy = num_xy(q)
        x = p_xy[0] + q_xy[0]
        y = p_xy[1] + q_xy[1]
        return xy_num(x,y)

    result = calc(p,q)
    print(f"##{tc} {result}")