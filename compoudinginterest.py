# Have the user enter their investment amount and expected interest
# Each year their investment wil increase by their invest + their investment * interest rate is
# Print the earnings after a 10 year period

# Ask for money invested + interest rate
money = input("Enter money invested: ")
interest = input("Enter interest rate: ")

# Convert the value to a float
money = float(money)

# Convert value to a float and round the percentage rate by 2 digits
interest = float(interest) * .01

# Cycle trough 10 years using a for loop and range from 0 to 9
for i in range(10):
    money = money + (money * interest)

# Output the results
print("Investment after 10 years: {:.2f}".format(money))
