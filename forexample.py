# for i in [2, 4, 6, 8, 10]:
#     print("i = ", i)
#
# for i in range(10):
#     print("i = ", i)
#
# for i in range(2, 10):
#     print("i = ", i)

# for loop excluding even numbers
for i in range(1,22):
    if (i % 2) != 0:
        print("i = ", i)

# 2 decimal places example
your_float = input("Enter a float: ")
your_float = float(your_float)
print("Round to 2 decimal places: {:.2f}".format(your_float))
