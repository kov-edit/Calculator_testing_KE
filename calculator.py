def sum(x, y):
    return x + y

def substraction(x, y):
    return x - y

def multiply(x, y):
    return x * y

def division(x, y):
    try:
        return x / y
    except ZeroDivisionError as e:
        return "Error: Cannot divide by zero"