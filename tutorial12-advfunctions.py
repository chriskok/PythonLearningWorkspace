# ---------- ADVANCED FUNCTIONS ----------

# ---------- FUNCTIONS AS OBJECTS ----------

def mult_by_2(num):
    return num * 2

# A function can be
# 1. Assigned to another name

times_two = mult_by_2

print("4 * 2 =", times_two(4))

# 2. Passed into other functions

def do_math(func, num):

    return func(num)

print("8 * 2 =", do_math(mult_by_2, 8))

# 3. Returned from a function

def get_func_mult_by_num(num):

    # Create a dynamic function that will receive a value
    # and then return that value times the value passed
    # into getFuncMultByNum()
    def mult_by(value):
        return num * value

    return mult_by

generated_func = get_func_mult_by_num(5)

print("5 * 10 =", generated_func(10))

# 4. Embedded in a data structure

listOfFuncs = [times_two, generated_func]

print("5 * 9 =", listOfFuncs[1](9))