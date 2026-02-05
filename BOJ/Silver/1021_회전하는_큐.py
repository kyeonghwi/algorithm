from collections import deque

n,m = map(int,input().split())
queue=deque([i for i in range(1,n+1)] )
arr = list(map(int,input().split()))
cnt=0
for elem in arr:
    while True:
        if queue[0]==elem:
            queue.popleft()
            break
        if queue.index(elem) <= len(queue)//2:
            temp = queue.popleft()
            queue.append(temp)
            cnt+=1
        else:
            temp = queue.pop()
            queue.appendleft(temp)
            cnt+=1
    
print(cnt)