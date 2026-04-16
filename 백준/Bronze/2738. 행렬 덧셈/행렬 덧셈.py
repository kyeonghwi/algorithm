import sys
input = sys.stdin.readline

# 1. 행렬의 크기 N, M 입력
n, m = map(int, input().split())

# 2. 첫 번째 행렬 (N x M 크기) 입력
arr1 = [list(map(int, input().split())) for _ in range(n)]

# 3. 두 번째 행렬 (N x M 크기) 입력
# ★★★ 이 부분이 핵심 수정사항입니다. 두 번째 행렬도 'n'개의 행을 가집니다.
arr2 = [list(map(int, input().split())) for _ in range(n)]

# 결과를 저장할 행렬을 만들 필요 없이, 바로 더해서 출력할 수도 있습니다.
for i in range(n):      # 행은 0부터 n-1 까지
    for j in range(m):  # 열은 0부터 m-1 까지
        # arr1의 (i, j) 원소와 arr2의 (i, j) 원소를 더해서 출력
        print(arr1[i][j] + arr2[i][j], end=" ")
    print() # 한 행의 출력이 끝나면 줄바꿈
