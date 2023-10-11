try:
    numerator = 10
    denominator = 0
    result = numerator / denominator  #  ArithmeticError
except ArithmeticError as e:
    print("Arithmetic Error:",' ',e)
