# Class1.py
class MyClass:
    def __init__(self):
        self._protected_field = "I'm protected"

    def _protected_method(self):
        return "This is a protected method"

from am1 import MyClass

class AnotherClass:
    def access_protected(self):
        obj = MyClass()
        print(obj._protected_field)   
        print(obj._protected_method()) 

class MyClass:
    def __init__(self):
        self._protected_field = "I'm protected"

    def _protected_method(self):
        return "This is a protected method"

from am1 import MyClass

class ChildClass(MyClass):
    def access_protected_from_child(self):
        print(self._protected_field)    
        print(self._protected_method())  


class MyClass:
    def __init__(self):
        self._protected_field = "I'm protected"

    def _protected_method(self):
        return "This is a protected method"

from am1 import MyClass

class AnotherClass:
    def access_protected_from_another_class(self):
        obj = MyClass()
        print(obj._protected_field)    
        print(obj._protected_method()) 

