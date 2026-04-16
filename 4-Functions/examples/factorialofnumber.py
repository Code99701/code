def factorial(n):
    """Returns the factorial of a number."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    

print(factorial(43)) 