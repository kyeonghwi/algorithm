n, m = map(int, input().split())
arr = list(map(int, input().split()))

result = 1 

for elem in arr:
    result = (result * elem) % m

print(result)
