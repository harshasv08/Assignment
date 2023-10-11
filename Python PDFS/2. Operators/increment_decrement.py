def increment(num):
    num += 1
    return num

def decrement(num):
    num -= 1
    return num

value = 5

value = increment(value)
print("After increment:", value)

value = decrement(value)
print("After decrement:", value)
