# python 3.9

def candidate_password(find, size, vowel, consonant, now_pass): # find = 현재 탐색 노드, size = 자릿수, vowel/consonant = 모음/자음 감소 수, now_pass = 현재 string
    if size <= 0:
        if vowel < 1 and consonant < 1: # 탐색이 완료되었고 조건을 만족한 경우
            print(now_pass)
        return
    
    for i in range(find, C): # 기준 노드 ~ 끝까지 탐색
        if candidate[i] in ['a', 'e', 'i', 'o', 'u']: # 모음일 때
            candidate_password(i + 1, size-1, vowel-1, consonant, now_pass + candidate[i])
        else: # 자음일 때
            candidate_password(i + 1, size-1, vowel, consonant - 1, now_pass + candidate[i])    
           

L, C = map(int, input().split()) # L = 자릿수 C = 예비 문자 수
candidate = sorted(input().split()) # 예비 문자 리스트
size = L 
vowels = 1 # 모음
consonants = 2 # 자음

candidate_password(0, size, vowels, consonants, "")