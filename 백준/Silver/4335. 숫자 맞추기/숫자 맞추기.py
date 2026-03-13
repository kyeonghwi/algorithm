import sys

# 입력 속도 향상
input = sys.stdin.readline
arr = []

while True:
    try:
        line = input().strip()
        if not line: break 
        n = int(line)
    except ValueError: break

    if n == 0:
        break

    s = input().strip() 

    if s == "right on":
        lie = False
        for guess, response in arr:
            if response == "too high" and not (guess > n):
                lie = True
            if response == "too low" and not (guess < n):
                lie = True
            
            if lie:
                break
        
        if lie:
            print('Stan is dishonest')
        else:
            print('Stan may be honest')
        
        arr = [] 
        
    else:
        arr.append((n, s))