class A:
    def __init__(self):
        self.varA = "Data A in Class A"

    def common_method(self):
        print("Common Method in Class A")

    def display_data(self):
        print(self.varA)


class B(A):
    def __init__(self):
        super().__init__()  
        self.varB = "Data B in Class B"

    def common_method(self):
        super().common_method()
        print("Common Method in Class B (Overridden)")

    def display_data(self):
        print(self.varB)


class C(B):
    def __init__(self):
        super().__init__()  
        self.varC = "Data C in Class C"

    def common_method(self):
        super().common_method()
        print("Common Method in Class C (Overridden)")

    def display_data(self):
        print(self.varC)

objB = B()
objC = C()

print("Calling overridden data members and methods with superclass reference for class B:")
super(B, objB).display_data()
super(B, objB).common_method()

print("\nCalling overridden data members and methods with superclass reference for class C:")
super(C, objC).display_data()
super(C, objC).common_method()
