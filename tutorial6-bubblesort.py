import random
import math

# 1. Outer loop decreases in size
# 2. Goal is to have largest at the end each time
# 3. Inner loop to compare indexes
# 4. Check if list[index] > list[index+1]
# 5. If so, swap
# 6. Decrement outer loop

numList = []

for item in range(10):
    # Note: randrange as suggested will be exclusive of the 9
    numList.append(random.randint(1, 9))

i = len(numList) - 1  # Note: using 0 index

while i > 0:
    j = 0
    while j < i:
        print("\nIs {} > {}".format(numList[j], numList[j+1]))
        if numList[j] > numList[j+1]:
            print("Switch")
            temp = numList[j]
            numList[j] = numList[j+1]
            numList[j+1] = temp
        else:
            print("No Switch")
        j += 1

        for k in numList:
            print(k, end=", ")
        print()

    print("END OF ROUND")

    i -= 1

print("\nFinal List: ")
for k in numList:
    print(k, end=", ")
print()
