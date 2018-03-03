numList = [i for i in range(1, 10)]

listOfValues = [[m * i for i in range(1, 10)]
                for m in numList]

for i in range(9):
    for j in range(9):
        print(listOfValues[i][j], end="\t")
    print()
print()
