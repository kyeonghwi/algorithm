import sys
from collections import defaultdict

input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
max_len = 0
start = 0
fruit = {}
for end in range(n):
    fruit[arr[end]] +=1

    while len(fruit) >2:
        fruit[arr[start]] -=1

        if fruit[arr[start]] ==0:
            del fruit[arr[start]]

        start+=1
    max_len = max(max_len, end - start +1)

print(max_len)