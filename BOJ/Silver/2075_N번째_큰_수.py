import heapq
n =int(input())

heap =[]
for _ in range(n):
    arr = list(map(int,input().split()))
    for elem in arr:
        if len(heap) <n:
            heapq.heappush(heap, elem)
        else :
            if heap[0] < elem:
                heapq.heappop(heap)
                heapq.heappush(heap, elem)
print(heap[0])