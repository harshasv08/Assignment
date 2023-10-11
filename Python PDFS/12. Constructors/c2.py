class Parent:
    def __init__(self, arg1=None, arg2=None):
        self.arg1 = arg1
        self.arg2 = arg2
        print("Parent Constructor")

class Child(Parent):
    def __init__(self, arg1, arg2, arg3):
        super().__init__(arg1, arg2)  # Call the constructor of the superclass
        self.arg3 = arg3
        print("Child Constructor")

if __name__ == "__main__":
    child_obj = Child(10, 20, 30)
    
    # arguments from both parent and child constructors
    print("arg1:", child_obj.arg1)
    print("arg2:", child_obj.arg2)
    print("arg3:", child_obj.arg3)
