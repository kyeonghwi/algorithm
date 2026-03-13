T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    a,b = map(int,input().split())
    c,d= map(int,input().split())

    def route(a,b,c,d):
        