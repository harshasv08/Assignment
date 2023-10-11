class MyClass:
    # static variable
    static_var = 0

    def __init__(self, value):
        self.instance_var = value

# Access the static variable through the class
print("Static variable through class:", MyClass.static_var)
