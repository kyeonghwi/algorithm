p, k = map(int, input().split())

if p > k :
    print(p- k +1)
elif p==k:
    print(0)
else:
    print(999-k + p +2)