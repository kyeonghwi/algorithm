T= int(input())
for tc in range(1,T+1):
    n,k = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    grade_num = n//10
    rank = 0
    score=[]
    for i in range(n):
        value = 0
        value = arr[i][0]*0.35 + arr[i][1]*0.45 + arr[i][2]*0.2
        score.append(value)
    grade = sorted(score, reverse=True)
    for i, elem in enumerate(grade):
        if elem == score[k-1]:
            rank =i
    grade_index = rank//grade_num
    print(f"#{tc} {grades[grade_index]}")