T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().strip()))

    date = True
    day=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    for i in range(len(arr)):
        if arr[4]==0:
            if int(str(arr[6]) + str(arr[7])) > day[arr[5]]:
                date = False
        elif arr[4]==1:
            if int(str(arr[6]) + str(arr[7])) > day[10 + arr[5]]:
                date = False
        else:
            date = False
    result =[]
    for i in range(len(arr)):
        if i ==4 or i==6:
            result.append("/")
        result.append(arr[i])

    if date:
        print(f"#{tc} {''.join(map(str,result))}")
    else:
        print(f"#{tc} {-1}")
