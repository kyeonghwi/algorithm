arr= list(map(int,input().split()))
total = 0
for elem in arr:
    total+=elem**2
print(total%10)