T = int(input())
for tc in range(1,T+1):
    n = int(input())
    total=0
    for i in range(1, n + 1):
        if i%2==1:
           total +=i
        else:
            total -=i
    print(f"#{tc} {total}")