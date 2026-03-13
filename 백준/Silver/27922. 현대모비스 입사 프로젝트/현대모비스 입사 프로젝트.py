import sys

input = sys.stdin.readline
n, k = map(int,input().split())
arr = []  

for _ in range(n):
    arr.append(list(map(int, input().split()))) 
    
sum01 = sorted(arr, key = lambda x:x[0]+x[1], reverse=True)
sum02 = sorted(arr, key = lambda x:x[0]+x[2], reverse=True)
sum12 = sorted(arr, key = lambda x:x[2]+x[1], reverse=True)

sum01_1 = 0
sum02_1 =0 
sum12_1=0
for i in range(k):
    sum01_1 += sum01[i][0]+sum01[i][1]
    sum02_1 += sum02[i][0]+sum02[i][2]
    sum12_1 += sum12[i][1] +sum12[i][2]
print(max(sum01_1, sum02_1, sum12_1))