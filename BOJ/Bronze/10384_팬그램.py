alphabet = list(range(97, 123))

for t in range(1, int(input()) + 1):
    pangram = input().strip().lower()  # strip 추가
    check = [0] * 26
    for i in pangram:
        if ord(i) in alphabet:
            check[ord(i) - 97] += 1

    if min(check) == 0:
        print(f"Case {t}: Not a pangram")
    elif min(check) == 1:
        print(f"Case {t}: Pangram!")
    elif min(check) == 2:
        print(f"Case {t}: Double pangram!!")
    elif min(check) == 3:
        print(f"Case {t}: Triple pangram!!!")