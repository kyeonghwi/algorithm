def solve():
    # 입력 받기
    S = input().strip()
    
    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowel_indices = []
    
    # 모음의 위치(1-based) 저장
    for i, char in enumerate(S):
        if char in vowels:
            vowel_indices.append(i + 1)
    
    # 모음이 하나도 없는 경우 강세를 줄 수 없음
    if not vowel_indices:
        print("-1")
        return

    last_char = S[-1]
    
    # 규칙 판단
    # 모음으로 끝나거나 n 또는 s로 끝나는 경우 -> 뒤에서 두 번째 모음
    if (last_char in vowels) or (last_char == 'n') or (last_char == 's'):
        if len(vowel_indices) >= 2:
            print(vowel_indices[-2])
        else:
            # 모음이 2개 미만이라 뒤에서 두 번째 모음을 찾을 수 없는 경우
            print("-1")
    # 그 외(n, s가 아닌 자음으로 끝나는 경우) -> 마지막 모음
    else:
        # 모음이 하나라도 있으면 마지막 모음은 무조건 존재함
        print(vowel_indices[-1])

if __name__ == "__main__":
    solve()