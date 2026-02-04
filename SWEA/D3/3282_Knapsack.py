T = int(input())
for tc in range(1, T + 1):
    n, k = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]

    dp=[0] * (k+1)

    for weight, value in arr:
        for j in range(k, weight -1, -1):
            dp[j] = max(dp[j], dp[j - weight] + value)

    print(f"#{tc} {dp[k]}")