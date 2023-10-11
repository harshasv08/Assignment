def remove_duplicates(arr):
    s = set(arr)
    l = list(s)

    return l

a = [1, 2, 2, 3, 4, 4, 5]
unique_elements = remove_duplicates(a)
print("Array after removing duplicates:", unique_elements)
