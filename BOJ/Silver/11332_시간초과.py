import math
C = int(input())

for _ in range(C):
    temp = input().split()
    S = temp[0]
    N, T, L = map(int, temp[1:])
    limit = (10 ** 8) * L
    if S == "O(N)":
        if N * T <= limit:
            print("May Pass.")
        else:
            print("TLE!")
    if S == "O(N^2)":
        if ((N ** 2) * T) <= limit:
            print("May Pass.")
        else:
            print("TLE!")
    if S == "O(N^3)":
        if ((N ** 3) * T) <= limit:
            print("May Pass.")
        else:
            print("TLE!")            
    if S == "O(2^N)":
        if ((2 ** N) * T) <= limit:
            print("May Pass.")
        else:
            print("TLE!")
    if S == "O(N!)":
        if (math.factorial(N) * T) <= limit:
            print("May Pass.")
        else:
            print("TLE!")