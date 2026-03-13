import sys

input = sys.stdin.readline
n = int(input())
if n < 100:
    print(n)
else:
    cnt = 99
    for num in range(100, n + 1):
        digits = list(map(int, str(num)))
        common_difference = digits[1] - digits[0]
        if digits[2] - digits[1] == common_difference:
            cnt += 1

    print(cnt)