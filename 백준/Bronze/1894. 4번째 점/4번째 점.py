import sys

# 여러 줄의 입력을 받기 위해 반복문 사용
for line in sys.stdin:
    # 입력받은 한 줄을 공백 기준으로 나누어 실수형으로 변환
    coords = list(map(float, line.strip().split()))
    if not coords:
        continue
    
    x1, y1, x2, y2, x3, y3, x4, y4 = coords
    
    # 각 점의 좌표를 튜플로 저장
    p1 = (x1, y1)
    p2 = (x2, y2)
    p3 = (x3, y3)
    p4 = (x4, y4)
    
    res_x, res_y = 0.0, 0.0
    
    # 공통점을 찾아 네 번째 점의 좌표를 계산
    if p1 == p3:
        # 공통점이 p1(p3)인 경우, 나머지 두 점은 p2, p4
        res_x = p2[0] + p4[0] - p1[0]
        res_y = p2[1] + p4[1] - p1[1]
    elif p1 == p4:
        # 공통점이 p1(p4)인 경우, 나머지 두 점은 p2, p3
        res_x = p2[0] + p3[0] - p1[0]
        res_y = p2[1] + p3[1] - p1[1]
    elif p2 == p3:
        # 공통점이 p2(p3)인 경우, 나머지 두 점은 p1, p4
        res_x = p1[0] + p4[0] - p2[0]
        res_y = p1[1] + p4[1] - p2[1]
    elif p2 == p4:
        # 공통점이 p2(p4)인 경우, 나머지 두 점은 p1, p3
        res_x = p1[0] + p3[0] - p2[0]
        res_y = p1[1] + p3[1] - p2[1]
        
    # 결과를 소수점 셋째 자리까지 형식에 맞춰 출력
    print(f"{res_x:.3f} {res_y:.3f}")

