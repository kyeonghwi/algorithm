import sys 
from collections import deque

flag = 0
ans =''
word=''

ary = input()

for i in ary:
    if i =='<':
        flag=1
        ans +=word[::-1]
        word=''
        ans+=i
    elif i =='>':
        flag=0
        ans+=i
        
    elif flag==1:
        ans+=i
        
    elif i==' ':
        ans+=word[::-1]
        ans+=' '
        word=''
        
    elif flag==0:
        word+=i
        
ans+=word[::-1]
print(ans)