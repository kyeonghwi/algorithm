T = int(input())
for tc in range(1, T+1):
    n= int(input())
    arr= list(map(int,input().split()))
    cnt =[0]*101
    for i in arr:
        cnt[i] +=1
    max_count = max(cnt)
    max_num = 100
    for num in range(100, -1, -1):
        if cnt[num] == max_count:
            max_num = num
            break
    print(f"#{tc} {max_num}")