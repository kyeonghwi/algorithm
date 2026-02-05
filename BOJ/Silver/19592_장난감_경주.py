import sys

# 빠른 입력을 위해 sys.stdin.readline 사용
input = sys.stdin.readline

def solve():
    T = int(input())

    for _ in range(T):
        n, x, y = map(int, input().split())
        arr = list(map(int, input().split()))
        
        my = arr[-1]           # 내 속도
        target = max(arr[:-1]) # 경쟁자들 중 가장 빠른 속도 (수정됨!)
        
        # 경쟁자 시간 (거리 / 속도)
        rival_time = x / target
        
        # 1. 부스터 없이도 이기는 경우
        if my > target:
            print(0)
            continue
        
        # 2. 부스터 최대치(y)를 써도 못 이기는 경우 (수정됨!)
        # 최대 부스터 사용 시 내 시간 계산
        if y >= x: 
            min_my_time = x / y
        else:
            min_my_time = 1 + (x - y) / my
            
        if min_my_time >= rival_time: # 내 최선 시간이 경쟁자보다 크거나 같으면 가망 없음
            print(-1)
            continue
        
        # 3. 여기서부터가 질문하신 부분 (이분 탐색)
        # 1 ~ y 사이에서 내가 이길 수 있는 최소 부스터 속도를 찾습니다.
        left = 1
        right = y
        ans = 0 # 정답을 저장할 변수
        
        while left <= right:
            mid = (left + right) // 2
            
            # mid 속도로 부스터 썼을 때 시간 계산
            if mid >= x:
                my_time = x / mid
            else:
                my_time = 1 + (x - mid) / my
            
            # 내가 경쟁자보다 빠르면(시간이 작으면)
            if my_time < rival_time:
                ans = mid       # 일단 기록해두고
                right = mid - 1 # 더 작은 부스터 속도도 가능한지 확인 (왼쪽 탐색)
            else:
                left = mid + 1  # 너무 느림, 부스터 속도를 높여야 함 (오른쪽 탐색)
                
        print(ans)

if __name__ == "__main__":
    solve()