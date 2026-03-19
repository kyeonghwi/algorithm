import sys
input= sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    li = list(map(int,input().split()))
    result = []
    while True: # 루프를 계속 돌며 new_li를 만들예정
        new_li = []
        for i in range(len(li)-1):
            new_li.append( abs((li[i+1]-li[i])) ) #new_li의 i번째에는 li[i+1] - li[i] 의 양수값이 들어간다.
        new_li.append(abs((li[-1]-li[0]))) #new_li의 마지막은 li의 마지막 - 첫번째이다.
        if new_li not in result: #루프를 돌고있지 않으면
            result.append(new_li) #계속만든다.
            li= new_li
        else:
            result.append(new_li) #한번이라도 중복되면, 루프를 돌고있단얘기
            li= new_li
            break

    k= result[-1]
    if sum(k) == 0: #만약 0으로만 이루어져있으면
        print("ZERO")
    else:#그렇지 않다면
        print("LOOP")