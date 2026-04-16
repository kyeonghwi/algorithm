N = int(input())
lotto = list(input())
cnt = 1
check = False
 
for i in range(N-1) :
	# 인접한 문자열 확인
    if abs(ord(lotto[i]) - ord(lotto[i+1])) == 1 :
        cnt += 1
    else :
        cnt = 1	# 그렇지 않은 경우 cnt 초기화
    
    # cnt가 5라면 break
    if cnt == 5 :
        check = True
        break
 
# 출력
if check :
    print('YES')
else :
    print('NO')