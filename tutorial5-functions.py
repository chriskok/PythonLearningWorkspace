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
