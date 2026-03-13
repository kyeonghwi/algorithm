T = 1
for tc in range(1, T + 1):
    n = input()
    temp =0
    for i in range(len(n)):
        temp += int(n[i])
    print(temp)