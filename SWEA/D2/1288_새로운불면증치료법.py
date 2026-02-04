T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    sheep= set()
    cnt=0

    while len(sheep) < 10:
        cnt += 1
        num = n * cnt
        sheep.update(str(num))

    print(f"#{tc} {num}")