import sys

def solve():
    # 입력 속도를 높이기 위해 sys.stdin.read 사용
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    D = int(input_data[1])
    
    monsters = []
    equipments = []
    
    # 몬스터와 장비 분리
    idx = 2
    for _ in range(N):
        A = int(input_data[idx])
        X = int(input_data[idx+1])
        if A == 1:
            monsters.append(X)
        else:
            equipments.append(X)
        idx += 2
        
    # 오름차순 정렬
    monsters.sort()
    equipments.sort()
    
    ans = 0
    m_idx = 0
    e_idx = 0
    
    # 몬스터를 모두 잡을 때까지 반복
    while m_idx < len(monsters):
        if D > monsters[m_idx]:
            # 몬스터를 잡을 수 있는 경우
            D += monsters[m_idx]
            ans += 1
            m_idx += 1
        else:
            # 몬스터를 잡을 수 없어 장비를 사용해야 하는 경우
            if e_idx < len(equipments):
                D *= equipments[e_idx]
                ans += 1
                e_idx += 1
            else:
                # 몬스터도 못 잡고 남은 장비도 없다면 게임 오버
                break
                
    # 몬스터를 모두 잡았다면, 남은 장비는 모두 획득 가능
    if m_idx == len(monsters):
        ans += len(equipments) - e_idx
        
    print(ans)

if __name__ == '__main__':
    solve()