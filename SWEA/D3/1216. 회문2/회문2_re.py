T= 10
for tc in range(1,T+1):
    n =int(input())
    arr= [list(input().strip()) for _ in range(100)]
    answer = 1
    def palindrome_row(x, y, a):
        if y + a <= 100:
            temp = arr[x][y:y+a]
            if temp == temp[::-1]:
                return True
        return False

    def palindrome_col(x, y, a):
        if x + a <= 100:
            temp = [arr[i][y] for i in range(x, x+a)]
            if temp == temp[::-1]:
                return True
        return False

    for a in range(100,0,-1):
        found = False
        for i in range(100):
            for j in range(100):
                if palindrome_row(i, j, a) or palindrome_col(i, j, a):
                    answer = a
                    found = True
                    break
            if found:
                break
        if found:
            break
    print(f"#{n} {answer}")