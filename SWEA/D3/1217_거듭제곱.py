T = 10
for tc in range(1, T+1):
    case= int(input())
    n,m = map(int,input().split())
    res = n**m
    print(f"#{case} {res}")