N = int(input())

data = []

for i in range(N):
    data.append(list(map(int, input().split())))


for i in data:
    answer = 100000

    for j in range(i[2] + 1):
        temp = max(i[0] * j, i[0] * (i[2] - j) + i[1] * i[3])

        answer = min(answer, temp)
    
    print(answer)