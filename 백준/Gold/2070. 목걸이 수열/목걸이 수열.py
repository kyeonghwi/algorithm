import sys

def solve():
    # 입력을 받습니다.
    s = sys.stdin.readline().strip()
    if not s:
        return

    n = len(s)
    i = 0
    result = []

    # Duval's Algorithm을 이용한 분해
    while i < n:
        j = i + 1
        k = i
        # s[i...j-1] 구간에서 가장 긴 린돈 단어 패턴을 찾습니다.
        while j < n and s[k] <= s[j]:
            if s[k] < s[j]:
                # s[j]가 더 크다면 이전의 주기성이 깨지고 더 긴 린돈 단어가 될 가능성이 생김
                # k를 시작점으로 초기화
                k = i
            else:
                # s[k] == s[j], 주기성 유지
                k += 1
            j += 1
        
        # 여기서 발견된 린돈 단어의 길이는 j - k 입니다.
        l = j - k
        
        # s[i...j-1] 구간은 린돈 단어 w가 (j-i)//l 번 반복되고, 
        # 뒤에 w의 접두사가 남은 형태입니다.
        # 문제 조건에 따라 동일한 목걸이 수열은 합쳐야 하므로, 
        # 완성된 반복 횟수만큼을 한 덩어리로 묶습니다.
        
        count = (j - i) // l
        sub_len = count * l
        
        # 묶음 추출
        component = s[i : i + sub_len]
        result.append(f"({component})")
        
        # 처리한 만큼 인덱스 이동
        i += sub_len

    # 결과 출력
    print("".join(result))

if __name__ == "__main__":
    solve()
