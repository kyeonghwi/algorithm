T= int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = [0]*n
    cnt=0

    def okay(row):
        for prev in range(row):
            if arr[prev] == arr[row] or abs(arr[row] - arr[prev]) == abs(row - prev):
                return False
        return True

    def dfs(idx):
        global cnt
        if idx==n:
            cnt+=1
            return
        for i in range(n):
            arr[idx] = i
            if okay(idx):
                dfs(idx+1)
        return cnt
    dfs(0)
    print(f"#{tc} {cnt}")