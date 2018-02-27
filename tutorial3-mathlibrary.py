import math
from decimal import Decimal as D

# we can access these methods by reference
# math.factorial, math.log(), math.trunc, math.log10()

print("ceil(10.3) =", math.ceil(10.3))
print("floor(10.3) =", math.ceil(10.3))

# Decimal calculations
sum = D(0)
sum += D("0.1")
sum += D("0.1")
sum += D("0.1")
sum -= D("0.3")

print('')
print("Sum =", sum)
print(".1 + .1 + .1 - .3 =", .1 + .1 + .1 - .3)

