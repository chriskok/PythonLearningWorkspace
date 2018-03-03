import random
import math

randList = ["string", 1.2423, 26]

oneToTen = list(range(10))

randList = randList + oneToTen

print(randList[0])

print(len(randList))

first3 = randList[0:3]

for i in first3:
    print("{} : {}". format(first3.index(i), i))

print(first3[0] * 3)

print("string" in first3)

print("Index of string:", first3.index("string"))

print("How many strings: ", first3.count("string"))

first3[0] = "New String"

for i in first3:
    print("{} : {}". format(first3.index(i), i))

first3.append("ANOTHER")

for i in first3:
    print("{} : {}". format(first3.index(i), i))