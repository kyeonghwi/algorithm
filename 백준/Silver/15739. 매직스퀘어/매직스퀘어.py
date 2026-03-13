import sys

def solve():
    # 빠른 입력을 위해 sys.stdin.readline 사용
    n = int(sys.stdin.readline())
    matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    # 1. 1부터 n^2까지의 숫자가 중복 없이 존재하는지 확인
    nums = []
    for row in matrix:
        nums.extend(row)

    if len(set(nums)) != n*n or min(nums) != 1 or max(nums) != n*n:
        print("FALSE")
        return

    # 2. 마방진의 합 계산 (첫 번째 행의 합을 기준으로 설정)
    magic_sum = sum(matrix[0])

    # 3. 가로 합 확인
    for r in range(n):
        if sum(matrix[r]) != magic_sum:
            print("FALSE")
            return

    # 4. 세로 합 확인
    for c in range(n):
        col_sum = 0
        for r in range(n):
            col_sum += matrix[r][c]
        if col_sum != magic_sum:
            print("FALSE")
            return

    # 5. 대각선 합 확인 (좌상 -> 우하)
    diag1 = 0
    for i in range(n):
        diag1 += matrix[i][i]
    if diag1 != magic_sum:
        print("FALSE")
        return

    # 6. 대각선 합 확인 (우상 -> 좌하)
    diag2 = 0
    for i in range(n):
        diag2 += matrix[i][n-1-i]
    if diag2 != magic_sum:
        print("FALSE")
        return

    print("TRUE")

solve()
