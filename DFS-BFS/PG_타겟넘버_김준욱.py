# -*- coding: utf-8 -*-
"""
Created on Fri May 13 02:39:41 2022

@author: JunWook Kim
"""

numbers = [int(x) for x in input().split()]
target = int(input())

result = []

def dfs(numbers, now):
    if len(numbers) == 0:
        result.append(now)
        return
    dfs(numbers[1:], now + numbers[0])
    dfs(numbers[1:], now - numbers[0])

    
dfs(numbers, 0)

answer = result.count(target)
print(answer)