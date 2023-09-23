# 1. Изучите тему и напишите другой способ нахождения простых чисел.
def is_prime_recursive(n, i=2):
    if n <= 1:
        return False
    elif i == n:
        return True
    elif n % i == 0:
        return False
    return is_prime_recursive(n, i + 1)


n = 100
prime_number = [num for num in range(2, n + 1) if is_prime_recursive(num)]
print(prime_number)
