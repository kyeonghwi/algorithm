import math

print("n e")
print("- -----------")
n=0
e=1
print(n, e)
for i in range(1,10):
    e +=1/math.factorial(i)
    n+=1
    print("%d %.9f" % (n, e))
