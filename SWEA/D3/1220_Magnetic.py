T = 10
for tc in range(1, T+1):
    case= int(input())
    arr= [list(map(int,input().split())) for _ in range(100)]
    deadlock = 0

    for i in range(100):
        mag = []
        for j in range(100):
            if arr[j][i] != 0:
                mag.append(arr[j][i])
        for a in range(len(mag)-1):
            if mag[a] ==1 and mag[a+1]==2:
                deadlock+=1
    print(f"#{tc} {deadlock}")
