class MyClass:
    # static variable
    static_var = 0

    def __init__(self, value):
        self.instance_var = value

# Create instances of the class
obj1 = MyClass(1)
obj2 = MyClass(2)

# Modify the static variable through an instance
obj1.static_var = 10  # This creates a new instance variable in obj1
print("Modified static variable through instance obj1:", obj1.static_var)
print("Static variable through instance obj2:", obj2.static_var)
