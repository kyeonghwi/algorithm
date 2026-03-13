import sys

input = sys.stdin.readline
a,b,c = map(int,input().split())

def power(a,b,c):
    if b==1:
        return a%c

    temp = power(a,b//2,c)
    result = (temp*temp) % c
    if b%2==1:
        result = (result*a)%c
    return result
print(power(a,b,c))