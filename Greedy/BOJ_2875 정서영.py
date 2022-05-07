n, m, k = map(int, input().split())
# n =여자 m=남자 k=인턴십
team = 0
if n >= 2*m:  # 남자 수에 맞춰서 팀 구성
    team = m  # 남자 수 = team개수
    n = n-2*m  # 남은 여자 수
    if n < k:  # 남은 사람으로 인턴십 인원을 채울 수 없으면
        k = k-n
        if(k % 3) == 0:
            team = team - (k//3)
        else:
            team = team - (k//3) - 1
else:  # 여자 수 기준
    team = n//2
    m = m - team
    if m < k:  # 남은 사람으로 인턴십 인원을 채울 수 없으면
        k = k-m
        if(k % 3) == 0:
            team = team - (k//3)
        else:
            team = team - (k//3) - 1

print(team)
