# Research the topic and write another way to find prime numbers.#


def is_prime_recursive(n, i=2):
    if n <= 1:
        return False
    elif i == n:
        return True
    elif n % i == 0:
        return False
    return is_prime_recursive(n, i + 1)
