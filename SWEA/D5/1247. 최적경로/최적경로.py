T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))

    loc =[]
    for i in range(0,(n+2)*2,2):
        loc.append((arr[i],arr[i+1]))

    min_dis = float('inf')
    def visit(i, visited, total, cnt):
        global min_dis
        if cnt==n:
            total += abs(loc[1][0] - loc[i][0]) + abs(loc[1][1] - loc[i][1])
            min_dis = min(min_dis, total)
            return

        for j in range(2,n+2):
            if not visited[j]:
                visited[j] = True
                new_total = total + abs(loc[j][0]-loc[i][0]) + abs(loc[j][1]-loc[i][1])
                if new_total < min_dis:
                    visit(j, visited, new_total, cnt + 1)
                visited[j] = False
    visited = [False] * (n+2)
    visited[0] = True
    visit(0,visited,0,0)
    print(f"#{tc} {min_dis}")