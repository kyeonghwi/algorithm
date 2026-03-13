import sys

input = sys.stdin.readline

while True:
    line = input().rstrip()
    if line=="#":
        break
    arr=set()
    for elem in line:
        if 'a' <=elem <='z' or 'A' <=elem <='Z':
            arr.add(elem.lower())
    print(len(arr))