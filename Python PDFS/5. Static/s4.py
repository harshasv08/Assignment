class MyClass:
    # static variable
    static_var = 0

    @classmethod
    def change_static_var(cls, new_value):
        # Change the static variable within the class
        cls.static_var = new_value

    @classmethod
    def get_static_var(cls):
        # Access the static variable within the class
        return cls.static_var

# Access the static variable through the class
print("Static variable before modification:", MyClass.get_static_var())

# Change the static variable within the class
MyClass.change_static_var(42)

# Access the modified static variable through the class
print("Static variable after modification:", MyClass.get_static_var())
