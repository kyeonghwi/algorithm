T = int(input())
for tc in range(1, T+1):
    a, n = input().split()
    n=int(n)
    arr=list(input().split())

    print(f"#{tc}")
    num =["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    cnt =[0] *10

    for i in range(n):
        temp = num.index(arr[i])
        cnt[temp] +=1
    result=[]
    for i in range(10):
        result.extend([num[i]] * cnt[i])
    print(*result)