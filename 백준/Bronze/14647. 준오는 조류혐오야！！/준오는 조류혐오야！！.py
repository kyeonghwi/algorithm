n, m = map(int, input().split())
bingo = []
row9Num, column9Num = [], []
for _ in range(n):
    tmp = list(map(str, input().split()))
    bingo.append(tmp)
    # 행 별 9의 개수 저장
    rowCnt9 = 0
    for t in tmp:
        rowCnt9 += t.count('9')
    row9Num.append(rowCnt9)

# 열 별 9의 개수 저장
for i in range(m):
    columnCnt9 = 0
    for j in range(n):
        columnCnt9 += bingo[j][i].count('9')
    column9Num.append(columnCnt9)

# 9의 총 개수 - 9가 제일 많은 행 또는 열의 9의 개수
print(sum(row9Num) - max(max(row9Num), max(column9Num)))