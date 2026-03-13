T = 10
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int,input().split()))
    found =False
    for _ in range(9999):
        for i in range(1,6):
             if arr[0] -i > 0:
                temp = arr.pop(0) -i
                arr.append(temp)
             else:
                arr.pop(0)
                arr.append(0)
                found=True
                break
        if found:
            break
    print(f"#{n}", end=" ")
    print(" ".join(map(str,arr)))
