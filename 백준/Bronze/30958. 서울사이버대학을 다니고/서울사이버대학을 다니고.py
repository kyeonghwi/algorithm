import sys

input = sys.stdin.readline
n = int(input())
arr = list(input())

alpha = [0 for _ in range(0, 26)]
for i in arr :
    if i == ' ' or i == ',' or i == '.' : 
        continue
    else : 
        alpha[ord(i)%97] += 1

print(max(alpha))