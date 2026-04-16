# (앞줄) 좌석 높이 + 키 < (뒷줄) 좌석 높이 + 키
# 주어진 조건에 맞게 모든 학생을 원하는 행의 좌석에 배치할 수 있는지 여부 출력

n, m, d = map(int, input().split())  # 행, 열, 높이 차이


# i+1줄, i행에 앉고자 하는 학생 m명의 키 / 키 + 단차 / 정렬
height = [sorted(h + d * (i + 1)
                 for h in map(int, input().split()))
          for i in range(n)]

chk = all(height[i][j] < height[i+1][j]
          for j in range(m)
          for i in range(n-1))

print("YES" if chk else "NO")