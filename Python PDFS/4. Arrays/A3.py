a = [10, 20, 30, 40, 50]

e = 30

try:
    index = a.index(e)
    print("The index of ",' ',e," is ",index)
except ValueError:
    print(e,"is not in the array")
