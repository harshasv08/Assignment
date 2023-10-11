
def arm_number(number):
    a_str = str(number)
    a_digits = len(a_str) 
    arm_sum = sum(int(digit) ** a_digits for digit in a_str)
    return number == arm_sum


num = int(input("Enter a number: "))
if arm_number(num):
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
