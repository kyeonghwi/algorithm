import sys
left = list(sys.stdin.readline().strip())
n = int(sys.stdin.readline())
right = []

for i in range(n):
    cmd = sys.stdin.readline().split()
    
    if cmd[0] == 'L':
        if left :
            right.append(left.pop())           
    elif cmd[0] == 'D':
        if right :
            left.append(right.pop())
    elif cmd[0] == 'B':
        if left :
            left.pop()
    elif cmd[0] =='P' :
        left.append(cmd[1])
            
answer = left + right[::-1]
print(''.join(answer))