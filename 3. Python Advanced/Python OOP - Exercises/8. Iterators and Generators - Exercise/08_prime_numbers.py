from math import sqrt


def get_primes(numbers):
    for num in numbers:
        prime = True

        if num <= 1:
            continue

        for i in range(2, int(sqrt(num) + 1)):
            if num % i == 0:
                prime = False
                break

        if prime:
            yield num


# Test code:

# print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
