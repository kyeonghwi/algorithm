import sys

input = sys.stdin.readline
s = list(map(int, list(input().strip())))
n = len(s)

found = False

for length in range(n, 1, -1):
    if length % 2 != 0: 
        continue
    
    for start in range(n - length + 1):
        end = start + length
        mid = start + (length // 2) 
        
        if sum(s[start:mid]) == sum(s[mid:end]):
            print(length)
            found = True
            break 
            
    if found:
        break 
