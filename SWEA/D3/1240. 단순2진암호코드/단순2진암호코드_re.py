T = int(input())
for tc in range(1, T + 1):
    n, m = map(int,input().split())
    arr= [list(map(int,input().strip())) for _ in range(n)]
    num = ['0001101', '0011001', '0010011','0111101', '0100011', '0110001', '0101111','0111011','0110111','0001011']

    cypher = []
    password=[]
    found = False
    for i in range(n):
        for j in range(m-1,-1,-1):
            if arr[i][j] == 1:
                for a in range(55,-1,-1):
                    cypher.append(arr[i][j-a])
                found = True
            if found:
                break
        if found:
            break
    if not found:
        print(f"#{tc} {0}")
        continue
    for i in range(0,56,7):
        temp = "".join(map(str,cypher[i:i+7]))
        password.append(num.index(temp))
    odd = sum(password[::2])
    even = sum(password[1::2])
    if (odd*3+even) %10==0:
        print(f"#{tc} {odd+even}")
    else:
        print(f"#{tc} {0}")