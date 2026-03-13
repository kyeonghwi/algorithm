T= 10
for tc in range(1,T+1):
    n = int(input())
    arr = list(map(int,input().split()))

    i = 1
    while arr[-1] > 0:
        temp = arr.pop(0)
        if temp - i > 0:
            arr.append(temp-i)
        else:
            arr.append(0)
        i = (i+1) % 6
        if i ==0:
            i+=1
    result = " ".join(map(str,arr))
    print(f"#{tc} {result}")
