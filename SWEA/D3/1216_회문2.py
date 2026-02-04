def is_palindrome(text):
    return text == text[::-1]

T = 10
for tc in range(1, T+1):
    n= int(input())
    matrix=[]
    for _ in range(100):
        matrix.append(list(input()))
    r_matrix = [list(row) for row in zip(*matrix)]
    max_len=1

    for length in range(100, 1, -1):
        if length <= max_len:
            break
        for i in range(100):
            if length <= max_len:
                break
            for j in range(0, 101 - length):
                if is_palindrome(matrix[i][j:j + length]):
                    max_len = length
                    break
                if is_palindrome(r_matrix[i][j:j + length]):
                    max_len = length
                    break
print(f"#{n} {max_len}")