A = int(input())
X = int(input())

div_num = 1_000_000_007
answer = 1
cur = A

# bin(X)[2:][::-1] 설명:
# 1. bin(X): X를 이진수 문자열로 변환 (예: 13 -> '0b1101')
# 2. [2:]: 앞의 '0b'를 떼어냄 ('1101')
# 3. [::-1]: 문자열을 뒤집음 ('1011') -> 낮은 자릿수(1, 2, 4, 8...)부터 처리하기 위함
for k in bin(X)[2:][::-1]:
    if k == '1':
        # 해당 비트가 1이면 현재 거듭제곱 값(cur)을 정답에 곱함
        answer = (answer * cur) % div_num
    
    # 다음 비트를 위해 cur를 제곱함 (A^1 -> A^2 -> A^4 -> A^8 ...)
    cur = (cur ** 2) % div_num

print(answer)