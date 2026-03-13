T = int(input())
for tc in range(1, T+1):
    n, m = map(int,input().split())
    arr=[list(map(int,input().strip())) for _ in range(n)]

    num = ['0001101', '0011001', '0010011','0111101', '0100011', '0110001', '0101111','0111011','0110111','0001011'] # 암호문 리스트
    result = 0
    temp=[]
    cypher=False
    for i in range(n):
        for j in range(m-1,-1,-1):
            if arr[i][j] == 1:
                decryption = arr[i][j-55:j+1]
                cypher =True
            if cypher:
                break
        if cypher:
            break
    if not cypher:
        print(f"#{tc} {result}")
        continue
    decryption_str = ''.join(map(str, decryption))
    for k in range(0,56,7):
         temp.append(num.index(decryption_str[k:k+7]))
    odd = sum(temp[::2])
    even = sum(temp[1::2])
    if (odd*3 + even)%10 ==0:
        result =odd + even
        print(f"#{tc} {result}")
    else:
        print(f"#{tc} {result}")