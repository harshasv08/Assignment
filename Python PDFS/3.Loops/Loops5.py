a = int(input("Enter the number:"))
b = int(input("Enter the 2nd number:"))
c = int(input("Enter the 3rd number:"))

if a >= b and a >= c:
    l = a
elif b >= a and b >= c:
    l = b
else:
    l = c

print("The largest number among", a,",", b, "and", c, "is:", l)