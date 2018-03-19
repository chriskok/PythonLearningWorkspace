# ---------- ANONYMOUS FUNCTIONS : LAMBDA ----------
# lambda is like def, but rather then assign the function
# to a name it just returns it. Because there is no name
# that is why they are called anonymous functions. You
# can however assign a lambda function to a name.

# This is their format
# lambda arg1, arg2,... : expression using the args

# lambdas are used when you need a small function, but
# don't want to junk up your code with temporary
# function names that may cause conflicts

# Add values
sum = lambda x, y : x + y

print("Sum :", sum(4, 5))

# Use a ternary operator to see if someone can vote
can_vote = lambda age: True if age >= 18 else False

print("Can Vote :", can_vote(16))

# Create a list of functions
powerList = [lambda x: x ** 2,
             lambda x: x ** 3,
             lambda x: x ** 4]

# Run each function on a value
for func in powerList:
    print(func(4))


# You can also store lambdas in dictionaires

attack = {'quick': (lambda: print("Quick Attack")),
           'power': (lambda: print("Power Attack")),
           'miss': (lambda: print("The Attack Missed"))}

attack['quick']()

# You could get a random dictionary as well for say our
# previous warrior objects
import random

# keys() returns an iterable so we convert it into a list
# choice() picks a random value from that list
attackKey = random.choice(list(attack.keys()))

attack[attackKey]()