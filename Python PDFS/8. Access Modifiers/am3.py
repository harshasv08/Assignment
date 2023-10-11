#Access public fields and methods from any class in the same package:

class MyClass:
    def __init__(self):
        self.public_field = "I'm public"

    def public_method(self):
        return "This is a public method"

from am1 import MyClass

class AnotherClass:
    def access_public(self):
        obj = MyClass()
        print(obj.public_field)    
        print(obj.public_method())


#Access public fields and methods from a class in a different package:

class AnotherClass:
    def access_public_from_another_class(self):
        obj = MyClass()
        print(obj.public_field)    
        print(obj.public_method())  
