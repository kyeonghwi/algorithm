import math
import sys

input = sys.stdin.readline
T= int(input())
for tc in range(T):
    n ,m = map(int,input().split())
    ans = math.comb(m,n)
    print(ans)