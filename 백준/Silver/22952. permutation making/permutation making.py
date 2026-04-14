import sys

def main():
    # 빠른 입력을 위한 sys.stdin.readline 사용
    n = int(sys.stdin.readline())
    
    # 결과를 담을 리스트 생성 (첫 번째 출력인 N을 미리 넣음)
    result = [n]
    
    # C++의 for (i = 1; i < N / 2; i++) 와 동일한 동작
    for i in range(1, n // 2):
        result.append(i)
        result.append(n - i)
        
    # N이 1이 아닐 때만 추가 작업 진행
    if n != 1:
        result.append(n // 2)
        
        # N이 홀수일 경우
        if n % 2 == 1:
            result.append(n // 2 + 1)
            
    # 리스트의 요소들을 공백을 기준으로 출력
    print(*result)

if __name__ == '__main__':
    main()