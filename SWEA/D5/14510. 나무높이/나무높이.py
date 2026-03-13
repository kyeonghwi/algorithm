T= int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = list(map(int,input().split()))
    if n == 0:
        print(f"#{tc} {0}")
        continue
    target_height = 0
    if n > 0:
        target_height = max(arr)
    total_ones_needed = 0
    total_twos_needed = 0

    for height in arr:
        diff = target_height - height
        if diff > 0:
            total_twos_needed += diff // 2
            total_ones_needed += diff % 2
    days_for_ones_expr = 2 * total_ones_needed - 1
    days_for_twos_expr = 2 * total_twos_needed

    result_days = max(days_for_ones_expr, days_for_twos_expr)

    print(f"#{tc} {result_days}")