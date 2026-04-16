import sys
from fractions import Fraction

input = sys.stdin.readline

def solve():
    # 첫 줄의 테스트 케이스 수 입력
    try:
        line = input().strip()
        if not line:
            return
        T = int(line)
    except ValueError:
        return

    for _ in range(T):
        # N: 고양이 수, M: 과자 종류 수
        line = input().split()
        if not line:
            break
        N, M = map(int, line)

        # 각 고양이가 먹은 총 양을 저장할 리스트 (초기값 0)
        # Fraction(0, 1)로 초기화하여 분수 연산 준비
        cats_total = [Fraction(0, 1) for _ in range(N)]

        for _ in range(M):
            data = list(map(int, input().split()))
            
            # data[0]은 조각 수 V, 그 뒤는 각 고양이가 먹은 조각 수
            V = data[0]
            pieces = data[1:]
            
            for i in range(N):
                # i번째 고양이가 먹은 양 = (먹은 조각 수) / (전체 조각 수 V)
                if pieces[i] > 0:
                    cats_total[i] += Fraction(pieces[i], V)

        # 가장 많이 먹은 양과 적게 먹은 양 계산
        max_val = max(cats_total)
        min_val = min(cats_total)
        
        # 차이 계산 (Fraction 객체끼리의 연산이므로 자동 통분/약분 됨)
        diff = max_val - min_val

        # 출력 조건: 정수라면 분모를 생략, 아니면 기약분수 형태 출력
        if diff.denominator == 1:
            print(diff.numerator)
        else:
            print(f"{diff.numerator}/{diff.denominator}")

if __name__ == "__main__":
    solve()