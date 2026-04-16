def addition(a, b):
    '''This function takes two numbers as input and returns their sum.'''
    return a + b

def subtraction(a, b):
    '''This function takes two numbers as input and returns their difference.'''
    return a - b

def multiplication(a, b):
    '''This function takes two numbers as input and returns their product.'''
    return a * b

def division(a, b):
    '''This function takes two numbers as input and returns their quotient.'''
    if b == 0:
        raise ValueError("The second argument cannot be zero.")
    return a / b