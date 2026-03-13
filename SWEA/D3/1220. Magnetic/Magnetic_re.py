T = 10
for tc in range(1, T+1):
    n= int(input())
    arr=[list(map(int,input().split())) for _ in range(100)]

    dead_lock = 0
    for j in range(100):
        temp=[]
        for i in range(100):
            if arr[i][j]!=0:
                temp.append(arr[i][j])
        for a in range(len(temp)-1):
            if temp[a]==1 and temp[a+1]==2:
                dead_lock+=1
    print(f"#{tc} {dead_lock}")