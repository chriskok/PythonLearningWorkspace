# Enter Calculation: 5 * 6
# 5 * 6 = 30

# Store user input
num1, operator, num2 = input('Enter calculation ').split()

# Convert strings to int
num1 = int(num1)
num2 = int(num2)

# if they enter + then, provide output based on addition
if operator == "+":
    print('{} + {} = {}'.format(num1, num2, num1 + num2))

# subtraction
elif operator == "-":
    print('{} - {} = {}'.format(num1, num2, num1 - num2))

# multiplication
elif operator == "*":
    print('{} * {} = {}'.format(num1, num2, num1 * num2))

# division
elif operator == "/":
    print('{} / {} = {}'.format(num1, num2, num1 / num2))

else:
    print('use either + - / or *')
