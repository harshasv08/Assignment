class MyClass:
    def __init__(self):
        self.__private_field = 42  # Private field

    def __private_method(self):
        print("This is a private method.")

    def print_private_field(self):
        print(f"Private Field: {self.__private_field}")

    def call_private_method(self):
        self.__private_method()

class SubClass(MyClass):
    def access_private_members(self):
        print("Accessing private members in SubClass:")
       


if __name__ == "__main__":
    obj = MyClass()
    
    obj.print_private_field()
    obj.call_private_method()
    
    sub_obj = SubClass()
    
    sub_obj.access_private_members()
