def find_duplicates(arr):
    element_counts = {}
    duplicates = []

    for i in arr:
        if i in element_counts:
            element_counts[i] += 1
        else:
            element_counts[i] = 1

    for i, count in element_counts.items():
        if count > 1:
            duplicates.append(i)

    return duplicates

my_array = [10, 20, 30, 10, 40, 20, 50]

duplicate_values = find_duplicates(my_array)
print("Duplicate values:", duplicate_values)
