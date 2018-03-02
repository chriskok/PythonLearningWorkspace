def add_nums(num1, num2):
    return num1 + num2


print("added:", add_nums(3,5))


# Anything define inside a function is only available there
def assign_name():
    name = "Doug"


# to change name method 1: return values
def changename(name):
    return "Mark"


name = "TOM"
name = changename(name)
print(name)

# to change name method 2: global variables
gbl_name = "sally"


def gbl_changename():
    global gbl_name
    gbl_name = "SAMMY"


gbl_changename()
print(gbl_name)


# No return value example
def get_sum(num1, num2):
    sum = num1 + num2


print(get_sum(3,4))


# MORE FUNCTIONS

# return multiple values
def mult_div(num1, num2):
    return (num1 * num2), (num1/num2)


mult, div = mult_div(5,4)
print("5 * 4 =", mult)
print("5 / 4 =", div)


# Not sure how many arguments
def sumAll(*args):
    sum = 0

    for i in args:
        sum+=i

    return sum


print("Sum: ", sumAll(1,2,3,4,5))
