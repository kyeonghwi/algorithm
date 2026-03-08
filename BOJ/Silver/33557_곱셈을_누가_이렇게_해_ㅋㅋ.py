import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    A, B = input().rstrip().split()

    C = int(A) * int(B)

    A_length = len(A)
    B_length = len(B)

    if A_length < B_length:
        A, B = B, A.rjust(B_length, '1')
    elif B_length < A_length:
        B = B.rjust(A_length, '1')

    D = int(''.join([str(int(a) * int(b)) for a, b in zip(A, B)]))

    if C == D:
        print(1)
    else:
        print(0)
