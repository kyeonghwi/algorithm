T = int(input())
for tc in range(1, T + 1):
    n, k = map(int,input().split())
    arr = list(map(int,input().split()))
    cnt=0

    def dfs(idx, total):
        global cnt
        if total == k:
            cnt+=1
            return
        if idx == n or total > k:
            return
        dfs(idx +1, total)
        dfs(idx+1, total+arr[idx])

    dfs(0,0)
    print(f"#{tc} {cnt}")