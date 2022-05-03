W, M, K = map(int, input().split())

# 여자 : 남자 = 2:1
team = 0
p = W + M # 전체인원 p

if W/M >= 2:
    team = M # 팀 개수
    p -= M * 3 # 팀에 참여한 사람 뺀 나머지
else:
    team = W / 2 # 팀 개수
    p -= team * 3


team_mem = team * 3 # 팀에 참여한 사람 수
if p < K:
    K = K - p
    if K < team_mem:
        team = (team_mem - K) / 3
    else: team = 0
    
print(int(team))




