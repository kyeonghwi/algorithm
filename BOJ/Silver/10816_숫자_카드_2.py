import sys
from collections import defaultdict

input = sys.stdin.readline
n = int(input())
arr1 = list(map(int,input().split()))
m = int(input())
arr2 = list(map(int,input().split()))
have = defaultdict(int)
for elem in arr1:
    have[elem] += 1
for card in arr2:
    print(have[card],end=" ")