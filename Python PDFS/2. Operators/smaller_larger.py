a = int(input("Enter the number:"))
b = int(input("Enter the 2nd number:"))

if a < b:
    s = a
    l = b
elif a > b:
    s = b
    l = a
else:
    print("Both numbers are equal.")

print("Smaller number:", s)
print("Larger number:", l)
