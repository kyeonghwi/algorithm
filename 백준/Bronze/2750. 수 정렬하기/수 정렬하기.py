n = int(input())
arr= [int(input()) for _ in range(n)]
arr.sort()
for elem in arr:
    print(elem)