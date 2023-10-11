def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b

result = divide(10, 2)  
print("Result:", result)

result = divide(10, 0)  
print("Result:", result)  
