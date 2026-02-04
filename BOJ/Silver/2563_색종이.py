n = int(input())
rect = []
for i in range(n):
    x, y = (map(int,input().split()))
    rect.append([x,y,x+10,y+10])
covered = set()
for x1, y1, x2, y2 in rect:
    for x in range(x1,x2):
        for y in range(y1,y2):
            covered.add((x,y))
print(len(covered))