T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int,input().split()))

    odd = 0
    for elem in arr:
        if elem%2==1:
            odd += elem
    print(f"#{tc} {odd}")