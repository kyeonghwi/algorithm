T = int(input())
for tc in range(1, T + 1):
    n,b = map(int,input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    s =sum(arr)

    min_height = s
    def dfs(idx, height):
        global min_height
        if min_height <height:
            return
        if idx==n:
            if b<= height <min_height:
               min_height = height
            return
        dfs(idx+1, height)
        dfs(idx+1, height+arr[idx])

    dfs(0,0)
    print(f"#{tc} {min_height - b}")