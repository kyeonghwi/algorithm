MOD = 1234567891


def nCr(n, r):
    if r == 0 or r == n:
        return 1
    r = min(r, n - r)

    numerator = 1
    for i in range(n, n - r, -1):
        numerator = (numerator * i) % MOD

    denominator = 1
    for i in range(1, r + 1):
        denominator = (denominator * i) % MOD

    return (numerator * pow(denominator, MOD - 2, MOD)) % MOD


T = int(input())
for tc in range(1, T + 1):
    n, r = map(int, input().split())
    print(f"#{tc} {nCr(n, r)}")
