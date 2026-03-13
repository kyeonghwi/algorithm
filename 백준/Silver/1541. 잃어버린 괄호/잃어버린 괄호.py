import sys

input = sys.stdin.readline
arr = list(input().strip())
x =0
formula = []
for i in range(len(arr)):
    if arr[i] == "+":
        formula.append(x)
        x = 0
        formula.append('+')
    elif arr[i] == "-":
        formula.append(x)
        x = 0
        formula.append('-')
    else:
        x = int(str(x) + str(arr[i]))
formula.append(x)
result = formula[0]
temp = 0
for j in range(1,len(formula)-1,2):
    if formula[j] == "-":
        if temp !=0:
            result -= temp
            temp = 0
        temp += formula[j+1]
    else:
        if temp!=0:
            temp +=formula[j+1]
        else:
            result +=formula[j+1]
result -=temp
print(result)