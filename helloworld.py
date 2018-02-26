# Prompt user input and store the variable
name = input('What is your name? ')

# Print out hello followed by the name they entered
print('Hello', name)

# Note: You can name a variable starting with letter or underscores
# Ask the user to input 2 values and store them as num 1 and num2
num1, num2 = input('Enter 2 numbers: ').split()

# Convert the strings into Integers
num1 = int(num1)
num2 = int(num2)

# Add the values entered and store in sum
sum = num1 + num2

# Subtract values and store in difference
difference = num1 - num2

# Multiply
product = num1 * num2

# Divide
quotient = num1 / num2

# Modulus
remainder = num1 % num2

# Print the results
print("{} + {} = {}".format(num1, num2, sum))
print("{} - {} = {}".format(num1, num2, difference))
print("{} * {} = {}".format(num1, num2, product))
print("{} / {} = {}".format(num1, num2, quotient))
print("{} % {} = {}".format(num1, num2, remainder))