T = 10
for tc in range(1, T+1):
    n= int(input())
    search = input()
    s = input()
    cnt=0
    for i in range(len(s)-len(search)+1):
        if search == s[i:i+len(search)]:
            cnt+=1
    print(f"#{tc} {cnt}")