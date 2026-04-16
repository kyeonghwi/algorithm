N = int(input())
arr = list(map(int, input().split()))
S = int(input())

for _ in range(S):
    i, j = map(int, input().split())
    if i == 1:  # 남학생
        for o in range(j, N + 1, j):
            arr[o - 1] = 1 - arr[o - 1]  # 스위치 토글
    else:  # 여학생
        j -= 1  # 인덱스 맞추기
        arr[j] = 1 - arr[j]  # 중앙 스위치 토글
        k = 1
        while True:
            if j - k >= 0 and j + k < N and arr[j - k] == arr[j + k]:
                arr[j - k] = 1 - arr[j - k]  # 왼쪽 스위치 토글
                arr[j + k] = 1 - arr[j + k]  # 오른쪽 스위치 토글
                k += 1
            else:
                break  # 대칭 조건이 깨지면 종료

# 결과 출력
for i in range(N):
    print(arr[i], end=' ')
    if (i + 1) % 20 == 0:
        print()
