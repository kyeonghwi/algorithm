T = int(input())
for tc in range(1, T + 1):
    arr = list(input())
    dic = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z',
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z',
           '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/']

    value =''
    for j in range(len(arr)):
        num = dic.index(arr[j])
        binary = str(bin(num)[2:])
        while len(binary) < 6:
            binary = '0' + binary
        value += binary
    result=''
    for k in range(len(arr)*6//8):
        temp = int(value[k*8: k*8+8], 2)
        result +=chr(temp)
    print(f"#{tc} {result}")
