import sys

input = sys.stdin.readline
s= input().strip()
t=input().strip()

s_repeat = s*len(t)
t_repeat = t*len(s)
if s_repeat == t_repeat:
    print(1)
else:
    print(0)