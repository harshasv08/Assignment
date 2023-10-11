class MyClass:
    def __init__(self, arg1=None, arg2=None):
        if arg1 is None and arg2 is None:
            print("Default Constructor: No arguments provided")
        elif arg2 is None:
            print(f"One Argument Constructor: arg1 = {arg1}")
        else:
            print(f"Two Argument Constructor: arg1 = {arg1}, arg2 = {arg2}")

if __name__ == "__main__":
    # the class to call all constructors
    obj1 = MyClass()
    obj2 = MyClass(10)
    obj3 = MyClass(20, 30)
