#시간초과..^^
def counting_duck(list):
    Duck = ['q','u','a','c','k']
    duck = 0
    duck_sound = 0
    remove = []
    k = 0
    
    while(list):
        if (len(list) % 5) !=0 or list[0]!='q':
            return -1
        for index,item in enumerate(list):
            if item == Duck[k]:
                if 0<=k<4:
                    k += 1
                    remove.append(index)
                else:#k=4
                    k = 0
                    remove.append(index)
                    duck_sound += 1
      
        if k==0:
            if duck_sound == 0:
                return -1
            else:
                #list 삭제 방식 변경
                #remove에 삭제하고싶은 인덱스를 담아주고,
                #해당 인덱스에 해당하는것을 삭제해줌
                #스택오버플로우 고마워
                #https://stackoverflow.com/questions/497426/deleting-multiple-elements-from-a-list/497439#497439
                list = [i for j, i in enumerate(list) if j not in remove]
                # print(list)       
        duck += 1
        remove.clear()
        duck_sound = 0
    return duck
record = input()
record = list(record)
print(counting_duck(record))    

            
            
    
    

