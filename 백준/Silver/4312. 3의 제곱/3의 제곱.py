import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n ==0:
        break
    n-=1
    a=0
    arr=[]
    while (1 << a) <= n:
        arr.append(3 ** a)
        a += 1
    p=[]
    for i in range(len(arr)):
        if n & (1<<i):
            p.append(arr[i])
    print('{ ', end = '')
    for i in p:
        if i == ' ':
            print('}')
            break
        elif i == p[-1]:
            print(f'{i}', end = ' ')
        else:
            print(f'{i}', end = ', ')
    print('}')