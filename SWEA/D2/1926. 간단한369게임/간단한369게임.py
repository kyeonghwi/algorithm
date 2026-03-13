T = 1
for tc in range(1, T + 1):
    n = int(input())

    for i in range(1,n+1):
        i = str(i)
        cnt=0
        for elem in i:
            if "3" in elem or "6" in elem or "9" in elem:
                cnt+=1
        i =int(i)
        if cnt ==0:
            print(i,end =" ")
        else:
            print("-" * cnt, end=" ")