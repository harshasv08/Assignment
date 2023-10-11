try:
    result = 5 / 0  # Attempting to divide by zero
except ArithmeticError as e:
    print(f"An Arithmetic Exception occurred: {e}")