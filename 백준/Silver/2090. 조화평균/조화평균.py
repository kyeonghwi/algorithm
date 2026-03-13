import sys
import math


def get_lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // math.gcd(a, b)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    n = int(next(iterator))

    values = [int(next(iterator)) for _ in range(n)]

    numerator = 1  # C++ 코드의 a
    denominator = values[0]  # C++ 코드의 b

    for i in range(1, n):
        curr_denom = values[i]
        curr_num = 1

        lcm_val = get_lcm(curr_denom, denominator)

        curr_num = (lcm_val // curr_denom) * curr_num

        numerator = (lcm_val // denominator) * numerator + curr_num
        denominator = lcm_val

    common_divisor = math.gcd(numerator, denominator)

    print(f"{denominator // common_divisor}/{numerator // common_divisor}")


if __name__ == "__main__":
    solve()