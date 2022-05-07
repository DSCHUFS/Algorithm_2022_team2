# -*- coding: utf-8 -*-
"""
Created on Mon May  2 21:32:35 2022

@author: JunWook Kim
"""
#python 
#n : 여자, m : 남자, k : 인턴쉽
n, m, k = map(int, input().split())

#남녀수를 2:1 비율로 비교, 한쪽 성별을 전부 포함하는 최대 팀을 구성
answer = 0
if (n / m) >= 2:
    answer = m
else:
    answer = int(n/2)
    
#팀을 구성하고 남은 인원수가 k보다 작으면 팀을 하나씩 해체, 남은 인원수가 k 이상이 될때까지 반복
while True:
    if ((n+m) - answer*3) >= k:
        break
    answer -= 1

print(answer)