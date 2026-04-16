i = int(input())
for k in range(i):
    n, s= input().split()
    for k in s:
        print(k*int(n), end='')
    print()