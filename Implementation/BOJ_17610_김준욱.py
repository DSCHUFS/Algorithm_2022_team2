# -*- coding: utf-8 -*-
"""
Created on Tue May 10 03:25:37 2022

@author: JunWook Kim
"""

k = int(input())
weight = [int(x) for x in input().split()]
maximum = sum(weight)       #입력받은 추들을 모두 사용하여 측정할 수 있는 최대 무게
answer_list = [False] * (maximum + 1)   #answer_list[측정 가능한 무게] = True
                                        #추후 False만 카운트하며 정답 표시

def solution(idx, now_weight):
    if(idx == k):
        answer_list[now_weight] = True
        return
    solution(idx + 1, now_weight)
    solution(idx + 1, now_weight + weight[idx])
    solution(idx + 1, abs(now_weight - weight[idx]))

solution(0, 0)

print(answer_list.count(False))