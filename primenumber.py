# Note, prime can only be divided by 1 and itself
# 5 is prime because only divided by 1 and 5 - positive factor
# 6 is not a prime, divide by 1,2,3,6


# use a for loop and check if modulus == 0 True
def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False

    return True


def get_prime(max_number):
    list_of_primes = []

    for num1 in range(2, max_number):
        if is_prime(num1):
            list_of_primes.append(num1)

    return list_of_primes


# Ask the user to type in the maximum prime
max_prime = input("Insert max prime: ")
max_prime = int(max_prime)

primes_list = get_prime(max_prime)

for prime in primes_list:
    print(prime)
