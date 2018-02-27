# Enter a string to hide in uppercase: HIDE

# Convert that to unicode numbers
# Secret Message: 34567890

# Original Message: HIDE

userInput = input("Enter a string to hide in uppercase: ")

# Cycle each character in the string and change to unicode
newString = ""
for char in userInput:
    newString += str(ord(char) - 23)

# Print the secret message
print("Secret Message:", newString)

# Cycle through each char 2 at a time and change the digits to characters
newOutput = ""
for i in range(0, len(newString)-1, 2):
    newOutput += chr(int(newString[i] + newString[i+1]) + 23)
    # print("int to convert:", int(newString[i] + newString[i+1]))

# Print the original message
print("Original Message:", newOutput)