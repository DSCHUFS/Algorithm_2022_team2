N, M = map(int,input().split())                     # N = 책 개수, M = 한 번에 들 수 있는 양
book_loc = list(map(int, input().split()))          # book_loc = 책 위치
distance = 0                                        # 이동 거리 저장

pos = []                                            # 양수 저장
neg = []                                            # 음수 저장

for i in book_loc:                                  # 음수-양수 분리
    if i < 0:
        neg.append(i)
    else:
        pos.append(i)


pos.sort(reverse=True)                              # 절댓값이 큰 순서로 정렬
neg.sort()

if len(neg) == 0:                                   # 모두 음수 or 양수인 경우 0 추가로 에러 방지
    neg.append(0)
elif len(pos) == 0:
    pos.append(0)


if abs(neg[0]) > pos[0]:                            # 음수 절대값 > 양수 절대값
    distance += abs(neg[0])                         # 가장 큰 절댓값 더하기
    for minus in range(M, len(neg), M):             # 가장 큰 절댓값 앞에서부터 제외 ~ 끝까지, M칸 띄우면서
        distance += abs(neg[minus]) * 2
    for plus in range(0, len(pos), M):              # 가장 앞에서부터 끝까지 M칸씩 띄우면서 
        distance += abs(pos[plus]) * 2
elif len(neg) == 0 or pos[0] >= abs(neg[0]):        # 양수 절대값 > 음수 절대값
    distance += pos[0]                              # 가장 큰 절대값 더하기
    for minus in range(0, len(neg), M):             # 가장 앞에서부터 끝까지 M칸씩 띄우면서
        distance += abs(neg[minus]) * 2
    for plus in range(M, len(pos), M):              # 가장 큰 절댓값 앞에서부터 제외 ~ 끝까지, M칸 띄우면서
        distance += abs(pos[plus]) * 2
    
    
print(distance)
