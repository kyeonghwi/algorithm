T = 10
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int,input().split()))
    k= int(input())
    command = list(input().split())

    i =0
    while i < len(command):
        if command[i] =="I":
            x = int(command[i+1])
            y = int(command[i+2])
            s= list(map(int,command[i+3:i+3+y]))
            arr[x:x] = s
            i += 3+y
        else:
            i+=1
    print(f"#{tc}", end=" ")
    print(*arr[:10])
