import sys
sys.stdin = open("input.txt", "r")

T = 10
for tc in range(1,T+1):
    N = int(input())
    stack  = []
    arr = list(input())
    result = 1
    for i in arr:
        if i in "({[<":
            stack.append(i)
        elif i == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                result = 0
                break
        elif i == "}":
            if stack and stack[-1] == "{":
                stack.pop()
            else:
                result = 0
                break
        elif i == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                result = 0
                break
        elif i == ">":
            if stack and stack[-1] == "<":
                stack.pop()
            else:
                result = 0
                break
    if stack:
        result = 0
    print(f"#{tc} {result}")