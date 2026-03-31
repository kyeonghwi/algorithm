K = bin(int(input()))[2:] #2진법으로 변환하여 풀이
answer = 0

for i in range(len(K)):
    if int(K[i]) == 1: #1인 부분만 3**n을 더해줌
        answer += 3 ** (len(K)-i-1)
print(answer)