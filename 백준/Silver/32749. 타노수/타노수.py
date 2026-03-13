import sys
input = sys.stdin.readline

n, t = map(int, input().split()) 
num = input().strip()

for _ in range(t):
    half = len(num) // 2
    
    left = num[:half]
    right = num[half:]
    
    if left > right:
        num = left
    else:
        num = right

print(num)