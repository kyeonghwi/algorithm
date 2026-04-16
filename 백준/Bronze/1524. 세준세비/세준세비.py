
import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    input()
    a, b = map(int, input().split()) #
    s_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

     # 병사들의 힘을 내림차순으로 정렬 (가장 강한 병사가 먼저 싸우도록)
    s_list.sort(reverse=True)
    b_list.sort(reverse=True)

    # 두 팀중 한쪽 팀의 병사가 전멸할때 까지 라운드 진행
    while s_list and b_list: # 두 팀 모두 병사가 남아있는 동안
        if s_list[0] >= b_list[0]:  # S팀 병사가 B팀 병사보다 강하거나 같다면
            b_list.pop(0)  # B팀의 가장 강한 병사를 제거
        elif s_list[0] < b_list[0]:  # B팀 병사가 S팀 병사보다 강하면
            s_list.pop(0)  # S팀의 가장 강한 병사를 제거
           
    if s_list:
        print('S')
    elif b_list:
        print('B')
    else:
        print('C')