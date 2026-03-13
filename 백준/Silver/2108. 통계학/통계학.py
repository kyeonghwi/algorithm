import sys
from collections import Counter

input = sys.stdin.readline
n = int(input())
arr= [int(input().strip()) for _ in range(n)]

print(round(sum(arr)/n))
arr.sort()
print(arr[(n-1)//2])
cnt = Counter(arr)
mode = max(cnt.values())
mode_dic=[]
arr_set = set(arr)
for i in arr_set:
    if mode == cnt[i]:
        mode_dic.append(i)
mode_dic.sort()
if len(mode_dic)>1:
    print(mode_dic[1])
else:
    print(mode_dic[0])
print(arr[-1] - arr[0])