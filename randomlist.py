import random

randList = []

for i in range(5):
    # Note: randrange as suggested will be exclusive of the 9
    randList.append(random.randint(1, 9))

print(randList)

