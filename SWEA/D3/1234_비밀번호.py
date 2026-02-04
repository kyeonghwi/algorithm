T = 10
for tc in range(1, T+1):
    n, arr = input().split()

    password=[]
    for elem in arr:
        if password and password[-1]==elem:
            password.pop()
        else:
            password.append(elem)

    print(f"#{tc} {''.join(password)}")