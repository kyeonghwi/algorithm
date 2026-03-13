T = int(input())
for tc in range(1, T + 1):
    n, m = map(int,input().split())
    arr = [list(input().strip()) for _ in range(n)]

    string_ex = ['0001101', '0011001', '0010011','0111101', '0100011', '0110001', '0101111','0111011','0110111','0001011']

    code = [[]for _ in range(10)]
    cnt=0
    for i in range(n):
        for j in range(m):
            if arr[i][j-1] =='0' and arr[i-1][j]=='0':
                a = 0
                while arr[i][j]!=0:
                    code[cnt].append(arr[i][j+a])
                    a+=1
    print(code[cnt])