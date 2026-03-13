import sys
from collections import Counter

input = lambda: sys.stdin.readline().rstrip()
n, m = map(int,input().split())

arr=Counter()
for _ in range(n):
    word = input()
    if len(word) >=m:
        arr[word]+=1
final_sorted = sorted(arr.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for elem,value in final_sorted:
    print(elem)