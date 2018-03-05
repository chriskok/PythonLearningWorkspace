# 1, 1, 2, 3, 5, 8, 13
# F(n) = F(n-1) + F(n-2)


def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)


num = int(input("How many fibonacci numbers? "))

for i in range(num):
    print("fibonacci #{}\t= {}".format(i, fibonacci(i)))
