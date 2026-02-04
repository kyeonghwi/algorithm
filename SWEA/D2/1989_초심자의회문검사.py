T = int(input())
for tc in range(1, T + 1):
    arr = list(input().strip())

    if arr==arr[::-1]:
        print(f"#{tc} {1}")
    else:
        print(f"#{tc} {0}")
