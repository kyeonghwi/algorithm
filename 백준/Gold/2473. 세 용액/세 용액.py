n=int(input())
arr=list(map(int,input().split()))
arr.sort()

min_value=3e9
answer=[]

for i in range(n-2):
    left=i+1
    right=n-1
    while left<right:
        if abs(min_value)>=abs(arr[left]+arr[i]+arr[right]):
            min_value=arr[left]+arr[i]+arr[right]
            answer=[arr[i],arr[left],arr[right]]
        if arr[left]+arr[i]+arr[right]<0:
            left+=1
        elif arr[left]+arr[i]+arr[right]>0:
            right-=1
        else:
            answer=[arr[i],arr[left],arr[right]]
            break

print(*answer)