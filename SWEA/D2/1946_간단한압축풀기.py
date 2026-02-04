T = int(input())
for tc in range(1, T+1):
    n= int(input())
    print(f"#{tc}")
    all =''
    for _ in range(n):
        s, num = input().split()
        all += s*int(num)
    for i in range(0, len(all), 10):
        print(all[i:i+10])