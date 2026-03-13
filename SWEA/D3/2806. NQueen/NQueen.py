T= int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [0] * n
    result = 0

    def is_safe(row):
        for prev in range(row):
            if arr[prev] == arr[row] or abs(arr[row] - arr[prev]) == row - prev:
                return False
        return True

    def dfs(row):
        global result
        if row == n:
            result+=1
            return
        for i in range(n):
            arr[row] = i
            if is_safe(row):
                dfs(row+1)
        return result

    dfs(0)
    print(f"#{tc} {result}")

