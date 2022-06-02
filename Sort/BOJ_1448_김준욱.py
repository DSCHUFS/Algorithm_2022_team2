import sys

n = sys.stdin.readline()
list = []
for x in range(int(n)):
    list.append(int(sys.stdin.readline()))

list.sort(reverse=True)
#print(list)
answer = -1

while len(list) >= 3:
    biggest = list[0]
    if biggest < list[1]+list[2]:
        answer = biggest + list[1] + list[2]
        break
    list = list[1:]
    #print(list)

print(answer)