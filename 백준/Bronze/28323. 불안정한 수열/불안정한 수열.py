N = int(input())
A = tuple(map(int, input().split()))

check = A[0] % 2

cnt = 1
for a in A[1:]:
    if a % 2 == 1 - check:
        cnt += 1
        check = 1 - check

print(cnt)