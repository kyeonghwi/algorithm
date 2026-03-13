import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
for _ in range(n):
    a,b = input().split()
    arr_a=list(a)
    arr_b=list(b)
    arr_a.sort()
    arr_b.sort()
    if arr_a==arr_b:
        print(a + " & "+ b +" are anagrams.")
    else:
        print(a + " & "+ b +" are NOT anagrams.")