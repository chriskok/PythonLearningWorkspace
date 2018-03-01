# Random Access Memory : RAM

# Enter string
user_input = input("Enter string: ")
input_list = user_input.split()

# Convert into an acronym
for i in input_list:
    print(i[0].upper(), end="")

