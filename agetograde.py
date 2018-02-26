# age is 5 -> Kindergarten
# age is 6 through 17, grades 1 through 12
# age is greater then 17 say go to college
# 10 or less lines

# Get age input
age = eval(input("Enter age: "))

# if age is 5 send to kindergarten
if age == 5:
    print("Kindergarten!")

# if less than 5
if age < 5:
    print("Too young!")

# age between 6 and 17 (inclusive)
elif (age >= 6) and (age <= 17):
    print("Grade {}!".format(age - 5))

# age greater than 17
elif age > 17:
    print("College!")
