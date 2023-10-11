def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return n % 2 != 0

n = int(input("Enter a number: "))

#  dictionary to emulate a switch-case statement
number_type = {
    True: "even",
    False: "odd"
}

result = number_type[is_even(n)]
print(f"{n} is {result}")
