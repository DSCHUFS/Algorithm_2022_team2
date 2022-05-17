#마지막 6번예제만 통과못함
#del이 너무 알아서 잘 삭제를 해버림
#for item in list안에 del을 넣으면 
#for문 돌릴때 자동으로 len이 계산이되서 안됨
def counting_duck(list):
    Duck = ['q','u','a','c','k']
    duck = 0
    duck_sound = 0
    
    k = 0
    if (len(list) % 5) !=0 or list[0]!='q':
        return -1
    while(list):
        for item in list:

            if item == Duck[k]:
                if 0<=k<4:
                    k += 1
                else:#k=4
                    k = 0
                    duck_sound += 1
      
        if k==0:
            if duck_sound == 0:
                return -1
            else:
                for _ in range(duck_sound):
                    list.remove('q')
                    # print(list)
                    list.remove('u')
                    # print(list)
                    list.remove('a')
                    # print(list)
                    list.remove('c')
                    # print(list)
                    list.remove('k')
                    # print(list)
        duck += 1
        print(list)
        duck_sound = 0
    return duck
record = input()
record = list(record)
print(counting_duck(record))    

# list.remove('q')
                    
#                     print("".join(list))
#                     list.remove('u')
#                     list.remove('a')
#                     list.remove('c')
#                     list.remove('k')
    
# global duck 
# duck = ['q','u','a','c','k']
# def complete(i):
#     if i == 'q':
#         return 1
#     elif i == 'u':
#         return 2   
#     elif i == 'a':
#         return 3 
#     elif i == 'c':
#         return 4 
#     elif i == 'k':
#         return 5 
# def quack(record):
#     global duck
#     #남은 record의 길이가 5로 나눠떨어지지않거나
#     #k부터 시작하면 quack을 시작할수없으므로
#     #바로 떨구기
    
#     if (len(record) % 5) !=0 or record[0]!='q':
#         return -1
#     while record:
#         ans = 0
#         for i in duck:
#             for j in record:
#                 if i==j:
#                     record.del(j)
#                     break
#                 else:
#                     continue
#             ans += complete(i)
            
                    
                    
#             if count >=1:
#                 return -1
            
            
    
    

