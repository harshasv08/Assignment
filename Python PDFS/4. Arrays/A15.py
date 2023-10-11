def count_even_and_odd(arr):
    e_count = 0
    o_count = 0

    for num in arr:
        if num % 2 == 0:
            e_count += 1
        else:
            o_count += 1

    return e_count, o_count

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
e_count, o_count = count_even_and_odd(a)
print("Number of even numbers:", e_count)
print("Number of odd numbers:", o_count)
