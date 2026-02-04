import sys
value = float('inf')

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
arr = list(map(int, input().split()))
x, y = 0, 0
l, r = 0, n - 1

while l < r:
    current = arr[l] + arr[r]

    if abs(current) < value:
        x = arr[l]
        y = arr[r]
        value = abs(current)

    if current == 0:
        break
    elif current < 0:
        l += 1
    else:
        r -= 1

print(x, y)
