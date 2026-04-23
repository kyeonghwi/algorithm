N = int(input())
S = input()
res = ''
for c in S:
    if c not in "JAVA":
        res += c
print(res if res else "nojava")