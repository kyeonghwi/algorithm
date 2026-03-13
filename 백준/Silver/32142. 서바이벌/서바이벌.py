import sys

# C++의 FASTIO와 유사하게 입력 속도를 높이기 위한 설정
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    
print(-1)
