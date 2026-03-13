import sys

input = lambda: sys.stdin.readline().rstrip()
while True:
    line = input()
    if not line:
        break
    n = int(line)
    result=set()
    k =1
    while len(result) <10:
        for elem in str(n*k):
            result.add(int(elem))
        k+=1
    print(k-1)