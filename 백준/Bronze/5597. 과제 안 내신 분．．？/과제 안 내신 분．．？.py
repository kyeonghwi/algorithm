st = [i for i in range(1,31)]
for i in range(28):
    n = int(input())
    st.remove(n)
print(min(st))
print(max(st))