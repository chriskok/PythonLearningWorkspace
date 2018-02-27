# Provide different output based on age
# 1 - 18 -> Important
# 21, 50, > 65 -> Important
# All else -> not important

# Receive age and store in age
age = eval(input("Enter age: "))

# and: if both conditions are true, return true
# or: if either condition is true, return true
# not: convert true to false, vice versa

# If age is greater than or equal to 1 and less than or equal to 18, print Important
if (age >= 1) and (age <= 18):
    print("Important Birthday")

# Age either 21 or 50 important
elif (age == 21) or (age == 50):
    print("Important Birthday")

# Check if age is less than 5 and the convert true to false and vice versa
elif not(age < 65 ):
    print("Important Birthday")

# Else not important
else:
    print("Not important birthday")

