import sys

input = sys.stdin.readline

line = input()
length =10
for i in range(1,len(line)-1):
    if line[i]==line[i-1]:
        length+=5
    else:
        length+=10
print(length)