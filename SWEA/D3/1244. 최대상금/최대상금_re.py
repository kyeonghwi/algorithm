T = int(input())
for tc in range(1, T + 1):
    ARR, N = input().split()
    n = int(N)
    arr = list(map(int, ARR))
    v= set()

    max_money=0
    def dfs(cnt):
        global max_money
        money = int(''.join(map(str, arr)))
        v.add((cnt, money))
        if (cnt, money) in v:
            return
        if cnt==n:
            if money > max_money:
                max_money = money
            return
        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                arr[i],arr[j] = arr[j],arr[i]
                dfs(cnt+1)
                arr[j], arr[i] = arr[i], arr[j]

    dfs(0)
    print(f"#{tc} {max_money}")