w = input()
s = input()
security = ""
alpa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
res = ""

# 암호화 키 생성
for ch in w:
    if ch not in security:
        security += ch

for ch in alpa:
    if ch not in w:
        security += ch

# 암호화
for ch in s:
    res += security[ord(ch) - 65]
print(res)
