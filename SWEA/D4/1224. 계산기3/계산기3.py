T = 10
for tc in range(1,T+1):
    N = int(input())
    arr = list(input())
    stack = []
    for i in arr:
        if i in "0123456789":
            stack.append(i)

