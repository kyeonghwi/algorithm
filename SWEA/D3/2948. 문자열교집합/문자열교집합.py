T = int(input())
for tc in range(1, T+1):
    N,M = map(int, input().split())
    A = list(input().split())
    B = list(input().split())

    #비어있는 set 선언
    #sa = set()
    # sa = set(A) print(sa)
    sa =set(A)
    sb = set(B)
    sc = sa & sb
    print(f'#{tc} {len(sc)}')