# Solve for X
# x + 4 = 9
# x will always be the 1st value and you only deal with addition

ori_str = input("Please input equation: ")
count = 0
val1 = 0
val2 = 0

for item in ori_str.split():
    if item.isdigit():
        if count == 0:
            val1 = int(item)
            count += 1
        elif count == 1:
            val2 = int(item)
            count += 1
        else:
            break


def solve_x(num1, num2):
    return num2 - num1


print("x =", solve_x(val1, val2))

# SOLUTION:
# Create a function that takes a string, splits it there, and then makes
# a new string "X = ans" to return. I can do that next time
# ALSO, he used x, add, num1, equal, num2 = equation.split() SO MUCH EASIER
 
