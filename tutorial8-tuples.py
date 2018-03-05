myTuple = (1,2,3,5,8)  # use tuple when you want a list but dont want values to change

print("1st val:", myTuple[0])

print(myTuple[0:3])

print("Tuple length:", len(myTuple))

moreFibs = myTuple + (13,21,34)

print("34?", 34 in moreFibs)

for i in moreFibs:
    print(i)

aList = [55, 89, 144]
aTuple = tuple(aList)
aList = list(aTuple)

print("Min:", min(aTuple))
print("Max:", max(aTuple))

