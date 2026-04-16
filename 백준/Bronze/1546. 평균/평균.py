n = int(input())
a = list(map(int, input().split()))
x = max(a)
for i in range(n):
    a[i] = a[i]/x*100
print(sum(a)/n)