a= []
for i in range(10):
    n = int(input())%42
    a.append(n)
print(len(set(a)))