# ---------- FUNCTION ANNOTATIONS ----------
# It is possible to define the data types of attributes
# and the returned value with annotations, but they have
# no impact on how the function operates, but instead
# are for documentation

def random_func(name: str, age: int, weight: float) -> str:
    print("Name :", name)
    print("Age :", age)
    print("Weight :", weight)

    return "{} is {} years old and weighs {}".format(name, age, weight)

print(random_func("Derek", 41, 165.5))

# You don't get an error if you pass bad data
print(random_func(89, "Derek", "Turtle"))

# You can print the annotations
print(random_func.__annotations__)