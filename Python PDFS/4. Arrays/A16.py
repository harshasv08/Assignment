def diff(arr):
    if not arr:
        return "Array is empty"

    max_value = arr[0] 
    min_value = arr[0] 

    for i in arr:
        if i > max_value:
            max_value = i
        elif i < min_value:
            min_value = i


    d = max_value - min_value

    return d

a = [12, 45, 2, 41, 31, 10, 8]
result = diff(a)
print("Difference between largest and smallest value:", result)
