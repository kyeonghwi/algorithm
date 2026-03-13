T = int(input())
for tc in range(1,T+1):
    arr = [list(map(int,input().split()))for _ in range(9)]
    sudoku = True
    for i in range(9):
        temp=set()
        for a in range(9):
            temp.add(arr[i][0 + a])
        if not len(temp) ==9:
            sudoku =False
    for i in range(9):
        temp=set()
        for a in range(9):
            temp.add(arr[0+a][i])
        if not len(temp) ==9:
            sudoku =False
    for i in range(0,9,3):
        for j in range(0,9,3):
            temp = set()
            for x in range(3):
                for y in range(3):
                    temp.add(arr[i + x][j + y])
        if not len(temp) ==9:
            sudoku =False
    if sudoku:
        print(f"#{tc} {1}")
    else:
        print(f"#{tc} {0}")
