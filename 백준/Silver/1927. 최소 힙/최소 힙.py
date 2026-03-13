import sys
import heapq
from heapq import heappush

input = sys.stdin.readline
n = int(input())
heap = []
for _ in range(n):
    x = int(input())
    if x ==0:
        if heap:
            print(heapq.heappop(heap))
            continue
        else:
            print(0)
            continue
    heapq.heappush(heap, x)
