T = int(input())
for tc in range(1, T + 1):
    n,m,k = map(int,input().split())
    arr = list(map(int, input().split()))
    arr.sort()

    wait = False
    bread=0
    cnt=0
    for i in range(n):
        prod = (arr[i] // m) * k  # 현재 손님 도착 시간까지 생산된 빵
        if prod < i + 1:  # (i+1)명의 손님을 모두 수용 가능한가?
            print(f"#{tc} {'Impossible'}")
            break
    else:
        print(f"#{tc} {'Possible'}")
