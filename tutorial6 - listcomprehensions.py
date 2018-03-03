import random
import math

evenList = [i * 2 for i in range(10)]
for j in evenList:
    print(j)
print()


numList = [1, 2, 3, 4, 5]
listOfValues = [[math.pow(m, 2), math.pow(m, 3), math.pow(m, 4), math.pow(m, 5)]
                for m in numList]
for i in listOfValues:
    print(i)
print()


multiDList = [[0] * 10 for i in range(10)]
multiDList[0][1] = 10
print(multiDList[0][1])
print()


listTable = [[0] * 4 for i in range(4)]

for i in range(4):
    for j in range(4):
        listTable[i][j] = "{} : {}". format(i,j)

for i in range(4):
    for j in range(4):
        print(listTable[i][j], end=" | ")
    print()
