#!/usr/bin/python3
"""determine the winner of the prime game"""


def isWinner(x, nums):
    """
    Determines the winner of a prime game played over multiple rounds.

    Parameters:
        x (int): The number of rounds.
        nums (list): An array where each element represents
        the value of n for that round.

    Returns:
        str: The name of the player that won the most rounds ("Maria" or "Ben")
        or None if the result is a tie.
    """
    def sieve_of_eratosthenes(max_num):
        """
        Generates a list of booleans indicating prime numbers up to max_num.

        Parameters:
            max_num (int): The upper limit to calculate primes.

        Returns:
            list: A boolean list where True indicates a prime number.
        """
        is_prime = [True] * (max_num + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(max_num ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, max_num + 1, i):
                    is_prime[j] = False
        return is_prime

    if x < 1 or not nums:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_count = [0] * (n + 1)
        count = 0

        for i in range(1, n + 1):
            if primes[i]:
                count += 1
            primes_count[i] = count

        if primes_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
