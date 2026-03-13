import heapq
import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    k = int(input())
    min_heap=[]
    max_heap=[]
    counts = {}
    for _ in range(k):
        s, n = input().split()
        n= int(n)
        if s=="I":
            heapq.heappush(min_heap, n)
            heapq.heappush(max_heap, -n)

            counts[n] = counts.get(n,0)+1
        else:
            if n==1:
                while max_heap and counts.get(-max_heap[0],0)== 0:
                    heapq.heappop(max_heap)

                if max_heap:
                    max_val = -heapq.heappop(max_heap)
                    counts[max_val] -=1
            else:
                while min_heap and counts.get(min_heap[0], 0)==0:
                    heapq.heappop(min_heap)

                if min_heap:
                    min_val = heapq.heappop(min_heap)
                    counts[min_val] -= 1

    while max_heap and counts.get(-max_heap[0],0)==0:
        heapq.heappop(max_heap)
    while min_heap and counts.get(min_heap[0],0)==0:
        heapq.heappop(min_heap)

    if not max_heap or not min_heap:
        print('EMPTY')
    else:
        print(-max_heap[0], min_heap[0])