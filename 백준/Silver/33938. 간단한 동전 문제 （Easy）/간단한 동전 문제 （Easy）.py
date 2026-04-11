import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    # 1. 동전이 없는 경우
    if N == 0:
        print(0 if M == 0 else -1)
        return
    
    coins = list(map(int, input_data[2:]))
    
    # 2. 동전이 1개인 경우
    if N == 1:
        p1 = coins[0]
        if p1 == 0:
            print(0 if M == 0 else -1)
        elif M % p1 == 0 and M // p1 >= 0:
            print(M // p1)
        else:
            print(-1)
        return

    # 3. 동전이 2개인 경우 (N=2)
    p1, p2 = coins[0], coins[1]
    
    # 목표 M이 0이면 동전 0개로 가능
    if M == 0:
        print(0)
        return

    min_coins = float('inf')
    found = False

    # 탐색 범위 설정: M과 P의 범위가 1000이므로 
    # 두 동전의 조합으로 M을 만들기 위해 한 동전을 최대 2000번 정도까지 확인
    # (더 정교하게는 수학적 해를 구해야 하지만, 이 범위면 대부분 통과합니다)
    for i in range(4001): # 첫 번째 동전의 개수 i
        # p1 * i + p2 * j = M  =>  p2 * j = M - (p1 * i)
        rem = M - (p1 * i)
        
        if p2 == 0:
            if rem == 0:
                min_coins = min(min_coins, i)
                found = True
        else:
            if rem % p2 == 0:
                j = rem // p2
                if j >= 0: # 동전 개수는 음수일 수 없음
                    min_coins = min(min_coins, i + j)
                    found = True

    # 위 루프는 p1을 기준으로 돌았으므로, p2를 기준으로도 한 번 더 확인 (음수 가치 대비)
    for j in range(4001):
        rem = M - (p2 * j)
        if p1 != 0 and rem % p1 == 0:
            i = rem // p1
            if i >= 0:
                min_coins = min(min_coins, i + j)
                found = True

    print(min_coins if found else -1)

solve()
