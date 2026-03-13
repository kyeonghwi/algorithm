T= int(input())
for tc in range(1, T+1):
    n, b = map(int,input().split())
    h = list(map(int,input().split()))

    min_sum = sum(h)

    def dfs(i, current_sum):
        global min_sum
        if i ==n:
            if current_sum >= b and current_sum < min_sum:
                min_sum = current_sum
            return
        dfs(i+1, current_sum + h[i])
        dfs(i+1, current_sum)

    dfs(0,0)
    print(f"#{tc} {min_sum - b}")



# from itertools import combinations
#
# T= int(input())
# for tc in range(1, T+1):
#     n, b = map(int,input().split())
#     h = list(map(int,input().split()))
#
#     min_sum = sum(h)
#
#     for i in range(1,n+1):
#         for comb in combinations(h, i):
#             s = sum(comb)
#             if s >=b and s < min_sum:
#                 min_sum = s
#     print(f"#{tc} {min_sum - b}")