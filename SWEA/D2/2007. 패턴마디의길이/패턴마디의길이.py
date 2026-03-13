T = int(input())
for tc in range(1, T + 1):
    arr = list(input().strip())

    found = False
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j]:
                if arr[i:j]==arr[j:j+j-i]:
                    start, end = i, j
                    found= True
                    break
        if found:
            break
    print(f"#{tc} {end - start}")