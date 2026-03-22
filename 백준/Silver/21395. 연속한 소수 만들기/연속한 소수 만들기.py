import sys
import bisect
import operator

def solve():
    # 입력을 한 번에 읽어와 I/O 병목을 제거합니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    T = int(input_data[0])
    
    # 넉넉하게 150,000까지의 소수를 구해둡니다 (에라토스테네스의 체)
    MAX_PRIME = 150000
    is_prime = [True] * (MAX_PRIME + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(MAX_PRIME**0.5) + 1):
        if is_prime[i]:
            is_prime[i*i : MAX_PRIME+1 : i] = [False] * len(range(i*i, MAX_PRIME+1, i))
            
    primes =[i for i in range(MAX_PRIME + 1) if is_prime[i]]
    
    idx = 1
    out =[]
    
    for _ in range(T):
        n = int(input_data[idx])
        x = [int(v) for v in input_data[idx+1 : idx+1+n]]
        x.sort()
        idx += 1 + n
        
        # 최적의 첫 번째 소수(primes[k])가 존재할 수 있는 수학적 최소/최대 인덱스 범위를 설정합니다.
        # 배열의 모든 요소보다 작거나 모든 요소보다 큰 범위는 애초에 탐색할 필요가 없습니다.
        k_min = max(0, bisect.bisect_left(primes, x[0]) - n)
        k_max = min(len(primes) - n, bisect.bisect_right(primes, x[-1]) + n)
        
        mid = n // 2
        # 가장 정답에 근접할 것으로 예상되는 중앙값 위치에서부터 바깥쪽으로 탐색을 시작합니다.
        approx_k = max(k_min, min(k_max, bisect.bisect_left(primes, x[mid]) - mid))
        
        min_cost = float('inf')
        
        stop_left = False
        stop_right = False
        
        max_d = max(approx_k - k_min, k_max - approx_k)
        
        for d in range(max_d + 1):
            if stop_left and stop_right:
                break
            
            # 오른쪽 방향 탐색 (소수 값이 커지는 방향)
            if not stop_right:
                k = approx_k + d
                if k <= k_max:
                    # 다중 포인트 가지치기: 단일 요소의 격차 중 하나라도 min_cost를 넘기면 즉시 중단
                    if (primes[k] - x[0] >= min_cost or 
                        primes[k + mid] - x[mid] >= min_cost or 
                        primes[k + n - 1] - x[-1] >= min_cost):
                        stop_right = True
                    else:
                        P = primes[k : k+n]
                        # 파이썬 C 레벨 연산으로 오버헤드 없이 리스트의 차이 절댓값의 합을 빠르게 계산합니다.
                        c = sum(map(abs, map(operator.sub, x, P)))
                        if c < min_cost:
                            min_cost = c
                else:
                    stop_right = True
                    
            # 왼쪽 방향 탐색 (소수 값이 작아지는 방향)
            if d > 0 and not stop_left:
                k = approx_k - d
                if k >= k_min:
                    # 다중 포인트 가지치기: 값이 작아지며 x 배열 요소와의 거리 오차가 min_cost를 넘기는지 확인
                    if (x[0] - primes[k] >= min_cost or 
                        x[mid] - primes[k + mid] >= min_cost or 
                        x[-1] - primes[k + n - 1] >= min_cost):
                        stop_left = True
                    else:
                        P = primes[k : k+n]
                        c = sum(map(abs, map(operator.sub, x, P)))
                        if c < min_cost:
                            min_cost = c
                else:
                    stop_left = True
                    
        out.append(str(min_cost))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()