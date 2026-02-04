import sys
input = sys.stdin.readline
n= int(input())
s = list(map(int,input().split()))
m= int(input())
s2 = list(map(int,input().split()))
result = []
for i in range(m):
    result.append('1' if s2[i] in s else '0')
print(' '.join(result))