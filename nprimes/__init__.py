"""
This program prints out a multiplication table of the first 10 primes.
- first row and column should have ten primes
"""
import sys


def is_prime(num):
    divisor = 2
    while divisor <= num ** 0.5:
        if num % divisor == 0:
            return False
        divisor += 1
    return True


def prime_generator(count):
    """
    naive prime solver using is_prime checks
    """
    num = 2
    n = 0
    while n < count:
        while not is_prime(num):
            num += 1
        yield num
        num += 1
        n += 1


def genprimes(n=10):
    return [p for p in prime_generator(n)]


def print_row(iterable, first_item):
    spacing = 10
    num_format = '{:-{}}'
    if not first_item:
        prefix = ' ' * spacing
    else:
        prefix = num_format.format(first_item, spacing)

    print(prefix + ''.join(num_format.format(v, spacing) for v in iterable))


def table(n=10):
    primes = genprimes(n)
    print_row(primes, first_item=None)
    for row in primes:
        print_row((row * col for col in primes), first_item=row)


if __name__ == '__main__':
    num = int(sys.argv[1])
    table(num)