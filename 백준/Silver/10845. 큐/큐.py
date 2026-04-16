import sys
n = int(sys.stdin.readline())
ans = []

for _ in range(n) :
    cmd = sys.stdin.readline().split()
    
    if cmd[0] =='push' :
        ans.append(cmd[1])
        
    elif cmd[0] =='pop':
        if ans:
            print(ans.pop(0))
        else:
            print(-1)
    elif cmd[0]=='size':
        print(len(ans))
    elif cmd[0]=='empty':
        if ans:
            print(0)
        else:
            print(1)
    elif cmd[0]=='front':
        if ans:
            print(ans[0])
        else:
            print(-1)
    elif cmd[0]=='back':
        if ans:
            print(ans[-1])
        else:
            print(-1)
    