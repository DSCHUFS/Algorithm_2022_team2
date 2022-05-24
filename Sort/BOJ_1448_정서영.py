import sys

n = int(sys.stdin.readline())
data = [int(sys.stdin.readline().strip()) for i in range(n)]

data.sort(reverse=True)  # 내림차순 정렬

tri = 0
len = len(data)-2
for i in range(len):
    if data[i+1] + data[i+2] <= data[i]:
        continue
    else:
        tri = data[i+1] + data[i+2] + data[i]
        break
if tri == 0:
    print(-1)
else:
    print(tri)
