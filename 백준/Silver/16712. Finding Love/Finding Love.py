import sys
input = sys.stdin.readline

n, m = map(int, input().split()) 
rank = list(map(int,input().split()))
out = list(map(int,input().split()))


for i in out:
    rank[:m] = sorted(rank[:m])
    rank.pop(i-1)
print(*rank)