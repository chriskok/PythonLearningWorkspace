# print(type(3))
# print(type(3.14))
# print(type("3"))
# print(type('3'))

samp_string = "Important string"
print(samp_string[0])
print(samp_string[-1])  # last index
print(samp_string[3+5])

print("length:", len(samp_string))  # get the strings length

print(samp_string[0:4])
print(samp_string[8:])

print("Green" + " eggs" * 5)

num_string = str(4) # Convert integer to string

# cycle through each character in string
# for char in samp_string:
#     print(char, end="")

for i in range(0, len(samp_string)-1, 2):
    print(samp_string[i] + samp_string[i+1])

# Note: A-Z 65-90, a-z 97-122

print("A =", ord("A"))
print("65 =", chr(65))
