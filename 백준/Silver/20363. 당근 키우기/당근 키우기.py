import math

x, y = map(int, input().split())  #온기, 수분

print(math.trunc(x + y + (min(x, y) / 10)))