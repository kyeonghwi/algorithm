import sys

T = int(input())

for tc in range(1, T+1):

    m, md, wd = map(int, sys.stdin.readline().split())
    ir = 0
    result = 0
    for i in range(m):
        q, r = divmod((md-ir), wd)
        if r == 0:
            result += q
            ir = 0
        else:
            if i == m-1:
                result += (q+1)
            else:
                result += (q+2)
            ir = wd - r
    print(f'Case #{tc}: {result}')