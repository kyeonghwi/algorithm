import heapq

n,k,t = map(int,input().split())
shark =list(map(int,input().split()))
shark.sort()
eat=[]
idx=0
for _ in range(k):
    while idx< n and shark[idx] <t:
        heapq.heappush(eat, -shark[idx])
        idx+=1

    if not eat:
        break
    largest = -heapq.heappop(eat)
    t += largest
print(t)