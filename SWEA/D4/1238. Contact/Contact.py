def bfs(start):
    q= []
    visited= [0] * 101
    q.append(start)
    visited[start] = 1
    while q:
        t= q.pop(0)

        for w in range(1,101):
            if adj_m[t][w] and visited[w] ==0:
                q.append(w)
                visited[w] = visited[t] +1
    max_idx = 1
    for i in range(2, 101):
        if visited[max_idx] <= visited[i]:
            max_idx = i
    return max_idx

T = 10
for tc in range(1, T+1):
    N , start = map(int, input().split())
    arr = list(map(int, input().split()))

    adj_m = [[0]*101 for _ in range(101)]
    for i in range(0, N ,2):
        n1, n2 = arr[i], arr[i+1]
        adj_m[n1][n2] = 1

    ans = bfs(start)
    print(f"#{tc} {ans}")
