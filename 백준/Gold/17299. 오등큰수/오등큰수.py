from collections import Counter

n = int(input())
a = list(map(int, input().split()))
result = [-1] * n
stack = [0]
counter = Counter(a)

for i in range(1,n):
    while stack and counter[a[stack[-1]]] < counter[a[i]] :
        result[stack.pop()] = a[i]
    stack.append(i)

print(*result)