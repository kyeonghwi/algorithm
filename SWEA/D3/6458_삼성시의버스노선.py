T = int(input())
for tc in range(1, T + 1):
    n =int(input())

    cnt=[0] * 5001

    for i in range(n):
        A, B = map(int, input().split())
        for j in range(A, B + 1):
            cnt[j] += 1
    p = int(input())
    bus_stop = [int(input()) for _ in range(p)]

    print(f"#{tc}", end=" ")
    for i in bus_stop:
        print(cnt[i], end=" ")
    print()