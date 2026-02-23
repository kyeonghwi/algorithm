import sys

# 입력 속도 향상을 위해 사용
input = sys.stdin.read

def solve():
    data = input().split()
    if not data:
        return
    
    # N: 마디 수, S: 초기 BPM, K: BPM 변화 횟수
    n = int(data[0])
    s = float(data[1])
    k = int(data[2])
    
    current_bpm = s
    current_measure = 1
    total_time = 0.0
    
    idx = 3
    # BPM 변화 정보 처리
    for _ in range(k):
        m = int(data[idx])      # 변화가 일어나는 마디 번호
        new_bpm = float(data[idx+1]) # 새로운 BPM
        
        # 이전 마디부터 현재 변화 마디 전까지의 시간 누적
        # 4박자 기준: (마디 차이 * 4박자) / (BPM / 60초) = (diff * 240) / BPM
        total_time += (m - current_measure) * 240 / current_bpm
        
        current_measure = m
        current_bpm = new_bpm
        idx += 2
    
    # 마지막 변화 지점부터 전체 마디 N까지의 남은 시간 계산
    total_time += (n + 1 - current_measure) * 240 / current_bpm
    
    # 소수점 아래 12자리까지 출력
    print(f"{total_time:.12f}")

if __name__ == "__main__":
    solve()
