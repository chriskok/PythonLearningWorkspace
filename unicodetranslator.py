# Enter a string to hide in uppercase: HIDE

# Convert that to unicode numbers
# Secret Message: 34567890

# Original Message: HIDE

userInput = input("Enter a string to hide in uppercase: ")

newString = ""
for char in userInput:
    newString += str(ord(char))

print("Secret Message:", newString)

newOutput = ""
for i in range(0, len(newString)-1, 2):
    newOutput += chr(int(newString[i] + newString[i+1]))
    #print("int to convert:", int(newString[i] + newString[i+1]))

print("Original Message:", newOutput)