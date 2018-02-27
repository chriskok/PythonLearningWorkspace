# How tall is the tree: 5
# 1 while loop and 3 for loops

    #
   ###
  #####
 #######
#########
    #

# 4 spaces: 1 hash
# 3 spaces: 3 hashes
# 2 spaces: 5 hashes
# ...
# 0 spaces: 9 hashes

# Need to do
# 1. Decrement spaces by 1 each time through the loop
# 2. Increment the hashes by 2 each time through the loop
# 3. Save spaces to the stump by calculating tree height
# 4. Decrement from tree height until it equals 0
# 5. Print spaces and then hashes for each row
# 6. Print stump spaces and then 1 hash

# Note: print('', end="") for space with no new line

# get user input
height = input("What is the height of your tree: ")
height = int(height)
initialSpaces = height - 1
increment = 1

# While loop checking going from height to 0
while height > 0:
    spaces = height - 1
    for s in range(spaces):
        print(' ', end="")
    for j in range(increment):
        print('#', end="")

    print('')
    increment += 2
    height -= 1

for s in range(initialSpaces):
    print(' ', end="")

print('#', end="")

