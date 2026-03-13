import sys

input = lambda: sys.stdin.readline().rstrip()
n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
a = int(input())

# 1. 각 열(Column)의 합을 미리 구합니다.
# col_sums[j] = j번째 열의 모든 행의 합
col_sums = [0] * m
for i in range(n):
    for j in range(m):
        col_sums[j] += arr[i][j]

# 2. 슬라이딩 윈도우로 연속된 a개 열의 합의 최댓값을 구합니다.
# 초기 윈도우 (0번째 ~ a-1번째 열의 합)
current_sum = sum(col_sums[:a])
max_sum = current_sum

# 윈도우를 한 칸씩 오른쪽으로 이동
# i는 새로 들어오는 열의 인덱스 (a 부터 m-1 까지)
for i in range(a, m):
    current_sum += col_sums[i]      # 오른쪽 열 추가
    current_sum -= col_sums[i-a]    # 왼쪽 열 제거
    max_sum = max(max_sum, current_sum)

print(max_sum)