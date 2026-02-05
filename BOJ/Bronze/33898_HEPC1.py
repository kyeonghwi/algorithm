line1 = input()
line2 = input()

A = line1[0]
B = line1[1]
C = line2[0]
D = line2[1]

cw_order = A + B + D + C

ccw_order = A + C + D + B

if "HEPC" in (cw_order * 2) or "HEPC" in (ccw_order * 2):
    print("YES")
else:
    print("NO")