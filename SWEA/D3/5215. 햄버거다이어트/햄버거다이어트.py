T= int(input())
for tc in range(1,T+1):
    n, l = map(int,input().split())
    t,k=[],[]
    for _ in range(n):
        T,K = map(int,input().split())
        t.append(T)
        k.append(K)

    max_taste = 0
    def dfs(idx, cal, taste):
        global max_taste
        if cal > l:
            return
        if idx==n:
            if taste >max_taste:
                max_taste = taste
            return
        dfs(idx+1, cal, taste)
        dfs(idx+1, cal+k[idx], taste+t[idx])

    dfs(0,0,0)
    print(f"#{tc} {max_taste}")
