N =int(input())

for _ in range(N):
    str= list(input().split())
    for i in str:
        print(i[::-1], end=" ")
    print()

