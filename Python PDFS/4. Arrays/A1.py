def sum(arr):
    total = 0
    for i in arr:
        if isinstance(i, int):
            total += i
    return total

a = eval(input("Enter the array list:"))
result = sum(a)
print("Sum of array values:", result)
