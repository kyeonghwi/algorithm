import sys

def main():
    # 입력 속도 최적화를 위해 sys.stdin.read 사용
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    
    checker = set()
    arr = []
    
    # 초기값 설정
    checker.add(1)
    arr.append(1)
    
    for _ in range(N):
        current_size = len(arr)
        # 현재 arr에 있는 원소들까지만 순회
        for j in range(current_size):
            for k in range(1, 10):
                tmp = arr[j] * k
                # 이전에 등장하지 않은 숫자라면 추가
                if tmp not in checker:
                    checker.add(tmp)
                    arr.append(tmp)
                    
    # 배열의 총 길이 출력
    print(len(arr))

if __name__ == '__main__':
    main()