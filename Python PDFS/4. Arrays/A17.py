def contains_elements(arr, element1, element2):
    return element1 in arr and element2 in arr

a = [1, 2, 12, 4, 23, 6, 7]
e1 = 12
e2 = 23

if contains_elements(a, e1, e2):
    print(f"The array contains both {e1} and {e2}.")
else:
    print(f"The array does not contain both {e1} and {e2}.")
