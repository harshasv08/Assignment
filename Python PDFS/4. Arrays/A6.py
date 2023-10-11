def copy_array(arr):
    return arr[:]

a = [10, 20, 30, 40, 50]

copied_array = copy_array(a)

print("Original array:", a)
print("Copied array:", copied_array)
