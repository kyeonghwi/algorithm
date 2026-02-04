T = int(input())
for tc in range(1, T+1):
    N = int(input())
    S = list(map(int, input()))
    count = 0
    max_count = 0
    for i in range(len(S)):
        if S[i] == 1:
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0

    print(f'#{tc} {max_count}')