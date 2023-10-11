class A:
    def common_method(self):
        print("Common Method in Class A")


class B(A):
    def common_method(self):
        super().common_method()
        print("Common Method in Class B (Overridden)")


class C(B):
    def common_method(self):
        super().common_method()
        print("Common Method in Class C (Overridden)")


objB = B()
objC = C()


print("Calling overridden method with superclass reference for class B:")
super(B, objB).common_method()

print("\nCalling overridden method with superclass reference for class C:")
super(C, objC).common_method()
