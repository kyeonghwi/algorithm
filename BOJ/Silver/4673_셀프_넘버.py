import sys

input = sys.stdin.readline
i=0
self_num = set()
while i < 10000:
    total = i
    for elem in str(i):
        total +=int(elem)
    self_num.add(total)
    i+=1
for j in range(1,10001):
    if j not in self_num:
        print(j)