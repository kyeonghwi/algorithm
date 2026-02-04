T = int(input())
for tc in range(1, T+1):
    case, n = input().split()
    n =int(n)
    arr = list(input().split())
    res=[0] *10

    s = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    for elem in arr:
        for i in range(10):
            if elem == s[i]:
                res[i]+=1
                break

    print(f"#{tc}")
    for i in range(10):
        for j in range(res[i]):
            print(s[i],end=" ")