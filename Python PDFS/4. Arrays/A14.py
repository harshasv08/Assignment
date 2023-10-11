def find_second_largest(arr):
    if len(arr) < 2:
        return "Array should contain at least two elements"

    arr.sort(reverse=True)

    return arr[1]

my_array = [12, 45, 2, 41, 31, 10, 8]
second_largest = find_second_largest(my_array)
print("The second largest number is:", second_largest)
