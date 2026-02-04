T = int(input())
for tc in range(1,T+1):
    n =int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    change= [0] * 8

    for i in range(8):
        if n//money[i] >0:
            change[i] = n//money[i]
            n = n%money[i]

    print(f"#{tc}")
    print(*change)


