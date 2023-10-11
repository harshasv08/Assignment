def arithmetic_operation(num1, num2, operator):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Division by zero is not allowed."
        result = num1 / num2
    else:
        return "Invalid operator"
    
    return result

num1 = int(input("Enter the number 1 value:"))
num2 = int(input("Enter the number 2 value:"))
operator = input("Enter the any operator :")
result = arithmetic_operation(num1, num2, operator)
print(f"{num1} {operator} {num2} = {result}")
