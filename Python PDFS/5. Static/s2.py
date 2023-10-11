class MyClass:
    # static variable
    static_var = 0

    def __init__(self, value):
        self.instance_var = value

# instances
obj1 = MyClass(1)
obj2 = MyClass(2)

# Access the static variable through an instance
print("Static variable through instance obj1:", obj1.static_var)
print("Static variable through instance obj2:", obj2.static_var)
