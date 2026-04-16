import sys
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T) : 
    n = int(input().rstrip())
    
    if n <= 2 : 
        print(1)
    else : 
        print(3)