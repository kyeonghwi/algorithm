import sys
import math

# 빠른 입출력을 위한 설정
input = sys.stdin.readline

def is_prime(n):
    """
    소수 판정 함수
    :param n: 판정할 정수
    :return: 소수이면 True, 아니면 False
    """
    if n <= 1:
        return False

    # 2부터 n의 제곱근까지 나누어 떨어지는지 확인
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solve():
    # N 입력
    try:
        line = input().strip()
        if not line: return # 빈 줄 처리
        n = int(line)
    except ValueError:
        return

    # 문제 로직: N + 1이 소수인지 확인
    if is_prime(n + 1):
        print(1)
        print(f"1 {n + 1}")
    else:
        print(0)

def main():
    # 테스트 케이스 개수 T 입력
    try:
        t_str = input().strip()
        if not t_str: return
        t = int(t_str)

        for _ in range(t):
            solve()

    except ValueError:
        return

if __name__ == "__main__":
    main()
