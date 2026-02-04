T = int(input())
for tc in range(1,T+1):
    arr = list(map(int,input().split()))
    value = sum(arr) - max(arr) -min(arr)
    average = value/8
    print(f"#{tc} {round(average)}")