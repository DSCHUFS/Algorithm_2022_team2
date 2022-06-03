#일단 다 오름차순해서..
#1,2,3,4,5를 빼면되지않나?
#11114 <- 12345
n = int(input())
score_org = [i for i in range(n)]
score_real = []
ans = 0
for _ in range(n):
    s = int(input())
    score_real.append(s)
score_real.sort()
for i in range(n):
    ans += abs(score_org[i] - score_real[i])
print(ans)