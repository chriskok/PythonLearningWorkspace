import random

# Generate random number from 1 to 50
rand_num = random.randrange(1,51)

# Increment this to be declared outside while loop
# i = 1
#
# while i != rand_num:
#     i += 1
#     print("i = ", i)
#
# print("The random value is: ", rand_num)

# Set the increment back to 1
i = 1

while i <= 20:
    if (i % 2) == 0:
        i += 1
        continue

    if i == 15:
        break

    print("Odd: ", i)
    i += 1
