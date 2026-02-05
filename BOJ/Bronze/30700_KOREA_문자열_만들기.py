import sys

input = sys.stdin.readline
s= list(input())
target = ["K","O","R","E","A"]

i = 0 
result=0
for elem in s:
    if elem == target[i]:
        i = (i+1)%5
        result+=1
print(result)