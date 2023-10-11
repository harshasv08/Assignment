def find_min_max(arr):
    if len(arr) == 0:
        return None, None 
    
    minimum = min(arr)
    maximum = max(arr)
    return minimum, maximum

my_array = [10, 20, 5, 30, 15]

min_value, max_value = find_min_max(my_array)
print("Minimum value:", min_value)
print("Maximum value:", max_value)
