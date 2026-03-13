T = int(input())
for tc in range(1, T + 1):
    m1, d1, m2, d2 = map(int,input().split())

    days=[0,31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    result = 0
    if m1 ==m2:
        result = d2-d1 +1
    else:
        result = days[m1] - d1 +1 + d2+ sum(days[m1+1:m2])
    print(f"#{tc} {result}")