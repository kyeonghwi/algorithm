arr = [] # 빈 list
for _ in range(9):
    arr.append(int(input()))

max_idx = 0
for i in range(1, 9):
    if arr[max_idx] < arr[i]:
        max_idx = i
print(arr[max_idx])
print(max_idx+1)