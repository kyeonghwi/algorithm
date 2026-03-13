T = int(input())
for tc in range(1, T+1):
    num, count = map(int,input().split())
    num_list = list(str(num))
    L= len(num_list)
    v = set()
    answer = 0

    def dfs(n):
        global answer
        if n == count:
            current = int("".join(num_list))
            if current > answer:
                answer = current
            return
        for i in range(L-1):
            for j in range(i+1,L):
                if num_list[i] != num_list[j]:
                    num_list[i], num_list[j] = num_list[j], num_list[i]
                    current_num = int("".join(num_list))
                    if (n, current_num) not in v:
                        v.add((n,current_num))
                        dfs(n+1)
                    num_list[i], num_list[j] = num_list[j], num_list[i]
    dfs(0)
    print(f"#{tc} {answer}")