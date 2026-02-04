T = int(input())
for tc in range(1, T+1):
    arr= list(map(int,input().strip()))
    time = 0
    temp=[0] * len(arr)
    for i in range(len(arr)):
        if temp[i] !=arr[i]:
            temp[i:] = [arr[i]] * (len(arr) -i)
            time +=1
        if temp == arr:
            break
    print(f"#{tc} {time}")