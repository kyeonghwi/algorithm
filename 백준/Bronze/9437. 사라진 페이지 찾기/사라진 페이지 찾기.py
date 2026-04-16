while(True):
    line = input().split()
    if line[0] == '0':
        break
    arr = list(map(int, line))
    n = arr[0]
    p =arr[1]
    for i in range(n//4):
        page = [2*i+1,2*i+2,n-2*i-1,n-2*i]
        if p in page:
            page.remove(p)
            print(*page)
            break;