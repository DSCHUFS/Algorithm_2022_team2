from collections import deque

N, K = map(int, input().split())
MAX_SIZE = 100001

queue = deque()
queue.append(N)

cnt = 0
time = [-1] * MAX_SIZE
time[N] = 0

while queue:
    node = queue.popleft()
    # 찾은 경우
    if node == K:
        cnt+=1
    # 못찾은 경우
    for child in [node * 2, node + 1, node - 1]: # 이동 가능한 다음 노드들
            # 1. 방문한 적이 없는 경우
            # 2. child node의 time이 현재 노드 + 1인 경우
            # -> 이 경우에는 트리의 탐색 구간에서 처음이라고 간주함
        if child > 100000 or child < 0:
            continue
        if time[child] == -1 or time[child] >= time[node] + 1: 
            time[child] = time[node] + 1
            queue.append(child)

print(time[K])
print(cnt)