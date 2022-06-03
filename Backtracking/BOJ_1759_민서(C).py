from itertools import combinations

L,C = map(int,input().split())
letters = list(input().split())
A = []#모음
B = []#자음
for i in letters:
    if i in ['a','e','i','o','u']:
        A.append(i)
    else:
        B.append(i)
A.sort()
B.sort()
ans = []
for i in range(1,L-1):#(1,2)
  D = list(combinations(A, i))#1
  E = list(combinations(B,L-i))#3
  for i in D:
    for j in E:
      temp = ''.join(sorted(i+j))
      ans.append(temp)
  D.clear()
  E.clear()
ans.sort()
for i in ans:
  print(i)
