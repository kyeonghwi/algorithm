import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
truth = arr[0]
if truth == 0:
    know = set()
else:
    know = set(arr[1:])

parties = []
for _ in range(m):
    arr1 = list(map(int, input().split()))
    party_set = set(arr1[1:])
    parties.append(party_set)

change = True
while change:
    change = False
    for party in parties:
        if know.intersection(party):
            before = len(know)
            know.update(party)
            if len(know) > before:
                change = True
gura = 0
for party in parties:
    if not know.intersection(party):
        gura += 1
print(gura)