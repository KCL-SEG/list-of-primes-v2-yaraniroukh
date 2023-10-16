"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def isPrime(n):
    if n < 2: return False
    else:
        for i in range(2, n):
            if n % i == 0: return False
        return True


def primes(number_of_primes):
    list = []
    if number_of_primes > 0:
        for i in range(2, 5*number_of_primes):
            if len(list) >= number_of_primes: break
            elif isPrime(i): list.append(i)
        return list
    else:
        raise ValueError()