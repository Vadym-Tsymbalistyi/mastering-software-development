# Print the numbers from 1 to 10 recursively.

def rec(n):
    print(n)
    if n < 10:
        rec(n + 1)


rec(1)
