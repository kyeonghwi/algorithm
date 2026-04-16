T = int(input())
for _ in range(T):
    stack = []
    S = input()
    for i in S:
        if i == "(":
            stack.append(i)
        elif i ==")":
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if stack:
            print("NO")
        else:
            print("YES")