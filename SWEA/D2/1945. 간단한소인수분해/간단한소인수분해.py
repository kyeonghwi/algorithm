T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [2,3,5,7,11]
    cnt = [0]*12
    for i in arr:
        while n%i ==0:
            n = n//i
            cnt[i] +=1
    print(f"#{tc}", end=" ")
    for i in arr:
        print(cnt[i],end=" ")
    print()