# python 3.9

N, M, K = map(int, input().split())

player = []
player_M = []
for _ in range(M):
    temp = list(map(float, input().split()))
    for i in range(0, N * 2, 2):
        player_M.append([int(temp[i]), temp[i+1]])
    player_M.sort(key=lambda x:x[0])
    player.append(player_M)
    player_M = []

max_ability = [0 for _ in range(N)]

for m in range(M):
    for n in range(N):
        if max_ability[n] < player[m][n][1]:
            max_ability[n] = player[m][n][1]


max_ability.sort(reverse=True)

total = 0
for k in range(K):
    total += max_ability[k]

print(round(total, 1))

# print(player)

