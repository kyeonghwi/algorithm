T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    
    floor={}
    
    for i in range(1,n+1):
        floor[i] = i
        
    for i in range(k):    
        for j in range(2,n+1):
            floor[j] = floor[j-1] + floor[j]
            
    print(floor[n])