#!/usr/bin/python3

"""Module calculate minmum operation to achieve n"""


def prime_numbers(n):
    """
    Generate a list of prime numbers up to a given number n.

    Args:
        n (int): The upper limit to generate prime numbers.

    Returns:
        List[int]: A list of prime numbers from 2 up to n.
    The function starts with the primes [2, 3]
    and checks all integers from 4 to n. If a number is not divisible
    by any previously found prime, it is added to the list.
    """
    if n == 2:
        return [2]
    if n == 3:
        return [3]

    primes = [2, 3]

    for i in range(4, n + 1):
        if not any(i % j == 0 for j in primes):
            primes.append(i)

    return primes


def unq_prime_factors(n):
    """
    Find the unique prime factors of a given number n.

    Args:
        n (int): The number to factorize into primes.

    Returns:
        List[int]: A list of prime factors of n.
    The function iteratively divides n by its smallest prime factor,
    which is found by calling the prime_numbers function,
    and continues until n becomes 1.
    """
    factors = []

    while n != 1:
        for i in prime_numbers(n):
            if n % i == 0:
                factors.append(i)
                n = n // i
                break

    return factors


def minOperations(n):
    """
    Calculate the minimum number of operations to
    achieve a string with n 'H' characters.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum number of copy-paste operations
        to reach n 'H' characters.
    The function returns 0 if n is less than or equal to 1. Otherwise,
    it sums the unique prime factors of n,
    as each prime factor represents a copy-paste cycle.
    """
    if n <= 1:
        return 0

    return sum(unq_prime_factors(n))
