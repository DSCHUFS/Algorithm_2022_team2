n, k = map(int, input().split(" "))
visited = [False] * 100001
time = 0

now = []
now.append(n)
visited[n] = True

temp = []

while now.count(k) < 1:
    for x in now:
        if x-1 >= 0:
            if not visited[x-1]:
                temp.append(x-1)
        if x+1 <= 100000:     
            if not visited[x+1]:
                temp.append(x+1)
        if 2*x <= 100000:
            if not visited[2*x]:
                temp.append(2*x)
    for x in temp:
        visited[x] = True
    now = temp
    temp = []
    time+=1

print(time)
print(now.count(k))