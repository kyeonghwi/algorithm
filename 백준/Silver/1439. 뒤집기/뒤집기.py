import sys

s = sys.stdin.readline().strip()

count0, count1 = 0, 0
prev = None

for ch in s:
    if ch != prev:
        if ch == '0':
            count0 += 1
        else:
            count1 += 1
    prev = ch

print(min(count0, count1))