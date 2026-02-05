import sys
input = sys.stdin.readline

n,m,q = map(int,input().split())
arr =[input().strip() for _ in range(m)]

for _ in range(q):
    input_values = input().split()
    string = input_values[0]
    x = int(input_values[1])
    y = int(input_values[2]) if len(input_values) > 2 else None
    if string == "assign":
        arr[x-1] = arr[y-1]
    elif string =="swap":
        arr[x-1], arr[y-1] = arr[y-1],arr[x-1]
    else:
        arr[x-1] = "0"

arr = [elem for elem in arr if elem != "0"]

print(len(arr))
for elem in arr:
    print(elem)