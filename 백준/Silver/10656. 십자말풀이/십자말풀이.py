import sys

# 입력을 빠르게 받기 위해 sys.stdin.readline 사용
input = sys.stdin.readline

def solve():
    # N(행), M(열) 입력
    N, M = map(int, input().split())
    
    # 격자 입력
    grid = [input().strip() for _ in range(N)]
    
    clue_starts = []

    for r in range(N):
        for c in range(M):
            # 현재 칸이 막혀있으면 건너뜀
            if grid[r][c] == '#':
                continue
            
            # 단서 시작점인지 확인하는 플래그
            is_clue = False
            
            # 1. 가로 단어 시작 조건 확인
            # 왼쪽이 벽이거나 범위 밖이고, 오른쪽으로 2칸 더 빈 칸이 있는지(총 3칸)
            if c + 2 < M:
                if (c == 0 or grid[r][c-1] == '#'):
                    if grid[r][c+1] == '.' and grid[r][c+2] == '.':
                        is_clue = True

            # 2. 세로 단어 시작 조건 확인
            # 위쪽이 벽이거나 범위 밖이고, 아래쪽으로 2칸 더 빈 칸이 있는지(총 3칸)
            if not is_clue and r + 2 < N:
                if (r == 0 or grid[r-1][c] == '#'):
                    if grid[r+1][c] == '.' and grid[r+2][c] == '.':
                        is_clue = True
            
            # 가로 혹은 세로 조건 중 하나라도 만족하면 결과에 추가
            if is_clue:
                clue_starts.append((r + 1, c + 1))

    # 결과 출력
    print(len(clue_starts))
    for r, c in clue_starts:
        print(f"{r} {c}")

if __name__ == "__main__":
    solve()