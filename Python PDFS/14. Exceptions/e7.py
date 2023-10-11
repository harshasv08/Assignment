try:
    x = int(input("Enter a number: "))
    result = 10 / x
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Please enter a valid number.")

finally:
    print("Finally block: This block always runs, regardless of exceptions.")
