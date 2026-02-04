import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n,m = map(int,input().split())
    team_score = [0]*n
    team_run = [0]*n
    pithagoras=[0]*n
    for _ in range(m):
        a,b,p,q =  map(int,input().split())
        team_score[a-1] +=p
        team_score[b-1] += q
        team_run[a-1] +=q
        team_run[b-1] +=p
    for i in range(n):
        if team_score[i]==0 and team_run[i]==0:
            pithagoras[i]=0
        else:
            pithagoras[i]=team_score[i]**2/(team_run[i]**2+team_score[i]**2)
    print(int(max(pithagoras)*1000))
    print(int(min(pithagoras)*1000))