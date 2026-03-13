import sys

input = lambda: sys.stdin.readline().rstrip()
t = int(input())
for tc in range(t):
    n = int(input())
    i=0
    result = set()
    while i<100:
        i+=1
        temp =n*i
        for elem in str(temp):
            result.add(int(elem))
        if len(result) == 10:
            break
    if len(result) == 10:
        print("Case #", (tc+1), ": ", n*i )
    else:
        print("Case #", (tc+1), ": INSOMNIA" )
