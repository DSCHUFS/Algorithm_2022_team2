from collections import deque

#입력
N, M = map(int,input().split())
path = []
for i in range(N):
    path.append(list(map(int,input().split())))

ry, rx, rd = map(int, input().split())
ey, ex, ed = map(int, input().split())
dir_x = [0, 1, -1, 0]
dir_y = [-1, 0, 0, 1]

right = [1, 3, 0, 2]
left = [2, 0, 3, 1]
#리스트에 들어가기위해서 인덱스처럼,..0부터 시작하게 
ry, rx, ey, ex = ry-1, rx-1, ey-1, ex-1
rd, ed = rd % 4, ed % 4
#결과값은 큐에 저장
q = deque()
q.append([0, rx, ry, rd])
#방문여부저장 3차원배열로
visited = [[[False]*4 for _ in range(M)] for _ in range(N)]
visited[ry][rx][rd] = True

def isZero(x, y):
    if 0 <= x < M and 0 <= y < N and path[y][x] == 0:
        return True
    return False

while q:
    count, x, y, d = q.popleft()
    if (x, y, d) == (ex, ey, ed):
        print(count)
        break
    #거리
    for i in range(1,4):#1,2,3만큼 움직일수있음
        try_x, try_y = x + dir_x[d] * i, y + dir_y[d] * i
        if isZero(try_x,try_y ):
            if not visited[try_y][try_x][d]:
                q.append([count+1, try_x, try_y, d])
                visited[try_y][try_x][d] = True
        else:
            break
    #방향
    for dir in ['right', 'left']:
        if dir == 'right':
            test_dir = right[d]
        else:
            test_dir = left[d]
        if not visited[y][x][test_dir]:
            q.append([count+1, x, y, test_dir])
            visited[y][x][test_dir] = True
            
            
# #입력
# #NxM행렬
# #M개가 N줄에 걸쳐 입력
# def robot(rx,ry,rd):
#     if rx >= N or rx<0 or ry>=N or ry<0:
#         return False 
#     if rx==wx and ry==wy:
#         if rd==wd:
#             return True
#         else:
#             for i in range(abs(wd-rd)):
#                 ans.append('t')
#             return True
            
#     if path[rx][ry] == '0':
#         if rd == 1:
#             if robot(rx+1,ry,rd):
#                 ans.append('g')
#                 return True
#         elif rd == 2:
#             if robot(rx-1,ry,rd):
#                 ans.append('g')
#                 return True
#         elif rd == 3:
#             if robot(rx,ry-1,rd):
#                 ans.append('g')
#                 return True
#         elif rd == 4 :
#             if robot(rx,ry+1,rd):
#                 ans.append('g')
#                 return True
#     ans = [g,g,g,t,g,t]
#     else:
#         if robot(rx+1,ry,rd):
#             for _ in range(abs(rd-1)):
#                 ans.append('t')
#             ans.append('g')
#             return robot(rx+1,ry,1)
#         elif robot(rx-1,ry,rd):
#             for _ in range(abs(rd-2)):
#                 ans.append('t')
#             ans.append('g')
#             return robot(rx-1,ry,2)
#         elif robot(rx,ry-1,rd):
#             for _ in range(abs(rd-3)):
#                 ans.append('t')
#             ans.append('g')
#             return robot(rx,ry-1,3)
        
#         elif robot(rx,ry+1,rd):
#             for _ in range(abs(rd-4)):
#                 ans.append('t')
#             ans.append('g')
#             return robot(rx,ry+1,4)
  
# ans = []  
# N,M = map(int,input().split())
# path = []
# for i in range(N):
#     path.append(list(map(int,input().split())))
# rx, ry, rd = map(int,input().split())
# wx, wy, wd = map(int,input().split())
# sol = robot(rx,ry,rd)
# if(sol):
#     print(len(ans))
#   #     elif rd==2:
# #         if(path[rx-rd,ry]==0):
# #     elif rd==3:
# #         if(path[rx,ry-rd]==0):
# #     elif rd==4: 
# #         if(path[rx,ry+rd]==0):
# # while(rx==wx and ry==wy and rd==wd):
# #     if rd==1:
# #         if(path[rx+rd,ry]==0):
# #     elif rd==2:
# #         if(path[rx-rd,ry]==0):
# #     elif rd==3:
# #         if(path[rx,ry-rd]==0):
# #     elif rd==4:
# #         if(path[rx,ry+rd]==0):
# #출발지점의 위치 행 열 방향
# #도착지점의 위치 행 열 방향
# #방향은 동쪽:1(+x) 서쪽:2(-x) 남쪽:3(-y) 북쪽:4(+y)
# #최소 명령어 횟수를 출력해라
# #1번은 궤도가 없어서 로봇이 갈수없는 지점
# #명령1)Go k(1,2,3)
# #명령2)Turn dir(1,2,3,4)