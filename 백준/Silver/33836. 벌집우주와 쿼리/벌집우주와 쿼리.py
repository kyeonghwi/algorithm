import sys

def solve():
    input = sys.stdin.readline
    Q = int(input())
    
    for _ in range(Q):
        x, y = map(int, input().split())
        
        # 0번 케이스
        if y == 0 and x >= 0:
            print(0)
        # 1번 케이스들
        elif x >= 0:
            print(1)
        elif y == 0 and x < 0:
            print(1)
        elif y < 0 and x >= y:
            print(1)
        # 그 외 모든 경우는 2번
        else:
            print(2)

if __name__ == '__main__':
    solve()
