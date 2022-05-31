l, c = map(int, input().split())
password = [x for x in input().split()]
password.sort()

answer = []     #정답 후보가 들어갈 변수

def check(answer):  #최소 모음1개, 자음2개가 포함되어있는지 확인하는 함수
    m, j = 0, 0
    if len(answer) == l:
        for x in answer:
            if x in ['a', 'e', 'i', 'o', 'u']:
                m += 1
            else:
                j += 1
    if (m >= 1 and j >= 2):
        return True
    else:
        return False    

def DFS(i, answer):
    if len(answer) == l or i == c:  #정답 후보의 사이즈가 l이거나 입력 index를 끝까지 탐색했다면
        if check(answer):           #모음과 자음 개수가 조건과 맞는지 확인
            for x in answer:
                print(x, end="")
            print()
        else:                       #조건과 맞지 않다면 backtrack
            return
    else:
        DFS(i+1, answer + [password[i]])    #password[i]를 정답 후보에 포함한채 다음 index 탐색
        DFS(i+1, answer)                    #password[i]를 정답 후보에 포함하지 않은채 다음 index 탐색

DFS(0, answer)