n = int(input())

# Powers of two must be positive.
if n <= 0:
    is_power_of_two = False
else:
    is_power_of_two = True
    # Repeatedly divide n by 2
    while n > 1:
        # If n is not divisible by 2 at any point, it's not a power of two.
        if n % 2 != 0:
            is_power_of_two = False
            break
        n = n // 2 # Use integer division

if is_power_of_two:
    print(1)
else:
    print(0)