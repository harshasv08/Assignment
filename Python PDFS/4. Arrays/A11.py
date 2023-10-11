def find_common_values(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    common_values = set1.intersection(set2)
    return list(common_values)

array1 = [10, 20, 30, 40, 50]
array2 = [30, 40, 50, 60, 70]

common_elements = find_common_values(array1, array2)
print("Common values:", common_elements)
