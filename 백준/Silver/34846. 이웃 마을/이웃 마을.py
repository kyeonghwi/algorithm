import sys
input = sys.stdin.readline

def solve():
    # 입력 처리
    try:
        line1 = input().split()
        if not line1: return
        N, M, Q = map(int, line1)
    except ValueError: return

    adj = [[] for _ in range(N + 1)]

    # 그래프 구성
    for _ in range(M):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    # 각 마을의 '이웃 중 역이 있는 마을의 수'를 저장할 배열
    neighbor_station_cnt = [0] * (N + 1)
    # 해당 마을에 역이 건설되었는지 체크
    has_station = [False] * (N + 1)

    results = []

    for _ in range(Q):
        query = list(map(int, input().split()))
        q_type, target = query[0], query[1]

        if q_type == 1:
            # 역 건설 (이미 건설된 경우 무시해야 시간복잡도 보장됨)
            if not has_station[target]:
                has_station[target] = True
                # 내 이웃들에게 "나 역 생겼어!" 라고 알림 (값 1 증가)
                for neighbor in adj[target]:
                    neighbor_station_cnt[neighbor] += 1
        else:
            # 미리 계산된 값 출력 (O(1))
            results.append(str(neighbor_station_cnt[target]))

    print('\n'.join(results))

if __name__ == '__main__':
    solve()
