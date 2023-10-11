def insert_element(arr, element, position):
    if position < 0 or position > len(arr):
        print("Invalid position. Element not inserted.")
        return arr  
    return arr[:position] + [element] + arr[position:]

a = [10, 20, 30, 40, 50]
insert = 25
insert_position = 2

modified_array = insert_element(a, insert, insert_position)

print("Original array:", a)
print("Modified array:", modified_array)

