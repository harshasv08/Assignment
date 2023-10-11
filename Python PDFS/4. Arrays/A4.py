def value(arr, value):
    return value in arr

a = [10, 20, 30, 40, 50]
find = 30

if value(a,find):
    print("The array contains ",' ',find)
else:
    print("The array does not contain."," ", find)
