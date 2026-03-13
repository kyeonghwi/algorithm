n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)

ans = 0
for i in range(min(m, (n+1)//2)):
    if arr[i] > 0:
        ans += arr[i]
    else:
        break

print(ans)
