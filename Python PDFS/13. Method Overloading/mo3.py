class a:
    def my_method(self, arg1, arg2):
        print(f"Method 1: arg1 = {arg1}, arg2 = {arg2}")

    def my_method(self, arg1, arg2):
        print(f"Method 2: arg1 = {arg1}, arg2 = {arg2}")

obj = a()

obj.my_method("Hello", "World")
