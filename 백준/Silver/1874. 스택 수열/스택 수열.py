n = int(input())
stack=[]
answer=[]
start =1

for _ in range(n):
    end = int(input())
    while start <= end:
        stack.append(start)
        answer.append('+')
        start +=1
        
    if stack[-1]== end :
        stack.pop()
        answer.append('-')
    else:
        print("NO")
        break
        
else:
    for i in answer:
        print(i)

