def bsearch(l, r, key, arr):
    while l<=r:
        m = (l+r)//2
        if arr[m] == key:
            return 1
        elif arr[m] < key:
            l = m+1
        else:
            r = m-1
    return 0

N = int(input())
arr1 = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))

arr1.sort()

for x in arr2:
    print(bsearch(0, N-1, x, arr1))