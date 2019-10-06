def is_prime(number):
    if number == 1:
        return False
    for i in range(number-2):
        if number % (i+2) == 0:
            return False
    return True

def primes():
    number = 2
    while True:
        if is_prime(number):
            yield number
        else:
            number++