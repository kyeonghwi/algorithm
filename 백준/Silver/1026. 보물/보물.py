import sys
input = sys.stdin.readline
n= int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
sorted_b = sorted(b)
sorted_a  =sorted(a, reverse= True)
result = 0
for i in range(n):
    result += sorted_b[i] * sorted_a[i]
print(result)