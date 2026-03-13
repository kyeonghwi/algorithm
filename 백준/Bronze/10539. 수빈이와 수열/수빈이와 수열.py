n = int(input())
arr=list(map(int,input().split()))

origin = []
current_sum=0
for i, elem in enumerate(arr):
    original_value = arr[i] * (i + 1) - current_sum
    
    origin.append(original_value)
    current_sum += original_value
print(*origin)