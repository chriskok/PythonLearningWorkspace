# Factorials
# eg: 3! = 3 * 2 * 1


def factorial(num):
    if num <= 1:
        return 1
    else:
        result = num * factorial(num - 1)
        return result


for i in range(20):
    print("{}!\t= {}".format(i, factorial(i)))
