T = int(input())
for tc in range(1,T+1):
    n = int(input())
    prev = []

    print(f"#{tc}")
    for i in range(n):
        now = []
        for j in range(i+1):
            if j==0 or j==i:
                now.append(1)
            else:
                now.append(prev[j-1] + prev[j])
        for num in now:
            print(num, end=" ")
        print()
        prev = now