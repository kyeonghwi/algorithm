T = 10
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int,input().split()))
    k= int(input())
    command = list(input().split())

    i =0
    while i < len(command):
        if command[i]=="I":
            x = int(command[i+1])
            y = int(command[i+2])
            s = list(map(int,command[i+3:i+3+y]))
            arr[x:x] = s
            i += y+3
        elif command[i]=="D":
            x = int(command[i + 1])
            y = int(command[i + 2])
            del arr[x:x+y]
            i += 3
        elif command[i]=="A":
            y = int(command[i + 1])
            s = list(map(int,command[i+2:i+2+y]))
            arr[-1:-1] = s
            i += y + 2

    print(f"#{tc}",end=" ")
    print(*arr[:10])