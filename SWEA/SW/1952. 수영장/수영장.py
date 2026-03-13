def f(n, s,d ,m, m3):
    global min_v
    if n>=13:
        if min_v > s:
            min_v = s
    else:
        f(n+1, s+min(use[]))

T = int(input())
for tc in range(1, T+1):
    d, m, m3, y = map(int(input().split()))
