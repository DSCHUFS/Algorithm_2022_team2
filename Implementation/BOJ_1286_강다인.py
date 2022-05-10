# python 3.9

student = int(input())                              # 학생 수
history = []                                        # 반 기록(2차원 배열)
classes = [[] for _ in range(10)]                   # 같은 반 학생을 저장할 배열
students = [[] for _ in range(student + 1)]         # 각 학생들의 동급생을 저장할 배열

for i in range(student):                            # 1학년부터 5학년까지 반배정 정보
    history.append(list(map(int, input().split())))

for grade in range(5):                              # 1학년부터 5학년까지
    for s in range(student):                        # 각 반에 학생들 배치
        classes[history[s][grade]].append(s + 1)
    for c in range(1, 10):                          # 모든 반에 대해
        if len(classes[c]) != 0:                    # 학생이 있으면
            for c_s in classes[c]:                  # 반의 모든 학생의 동급생을 서로 저장
                for c_ss in classes[c]:
                    students[c_s].append(c_ss)
    classes = [[] for _ in range(10)]               # 반 초기화

for sett in range(student + 1):                     # 집합으로 중복 제거
    students[sett] = set(students[sett])

max_index = 0
for m in range(1, student + 1):                     # 가장 많은 동급생을 가진 학생 번호 검색
    if len(students[m]) > len(students[max_index]):
        max_index = m

print(max_index)

