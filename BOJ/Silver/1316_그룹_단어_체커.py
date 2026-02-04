import sys

input = sys.stdin.readline
n = int(input())
cnt=0
for _ in range(n):
    gw = True
    word = input().strip()
    temp = []
    prev=''
    for elem in word:
        if elem != prev:
            if elem in temp:
                break
            temp.append(elem)
            prev = elem
    else:
        cnt+=1
print(cnt)