class a:
    def __init__(self):
        self.public_var = "I'm public"

    def _protected_method(self):
        print("This is a protected method")

    def __init__(self):
        self.__private_var = "I'm private"

    def public_method(self):
        print("This is a public method")

if __name__ == "__main__":
    obj = a()

    print(obj.public_var)  
    obj.public_method()    

    obj._protected_method()  

    print(obj._MyClass__private_var)  
