n = int(input())
num = [*map(int, input().split())]

cnt_odd = 0 
cnt_even = 0
left_odd = 0 # 왼쪽에 홀수를 모으는 경우
left_even = 0 # 왼쪽에 짝수를 모으는 경우

for i in num:
  if i%2 == 1:
    cnt_odd += 1
    left_odd += cnt_even
  else:
    left_even += cnt_odd
    cnt_even += 1

print(min(left_even, left_odd))