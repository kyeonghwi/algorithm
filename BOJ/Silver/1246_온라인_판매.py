import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
arr = [int(input()) for _ in range(m)]

# 오름차순 정렬
arr.sort()

max_profit = 0
best_price = 0

for i in range(m):
    can_sell = min(n, m - i)
    
    profit = arr[i] * can_sell
    
    if profit > max_profit:
        max_profit = profit
        best_price = arr[i]

print(best_price, max_profit)