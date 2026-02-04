T = 1
for tc in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()

    print(f"{arr[n//2]}")