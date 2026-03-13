import sys

input = sys.stdin.readline
n, m = map(int,input().split())

arr = [list(input().split()) for _ in range(n)]
dic = {name:pw for name,pw in arr}
for _ in range(m):
    site = input().strip()
    print(dic[site])